#import the neccesary libraries
from gql import gql, Client
import pandas as pd
from gql.transport.requests import RequestsHTTPTransport
import json
import asyncio
from datetime import datetime
import json
import os
import time
import glob
pd.set_option('display.max_columns', None)


def get_connection(url, header):
  header = header
  transport = RequestsHTTPTransport(url,headers=header,use_json=True)
  return Client(transport=transport, fetch_schema_from_transport=True)


def fetch_initial_data():
    query = gql('''
        { 

      nftTrades(limit: 1000) {
          chain
    collectionAddress
    collectionName
    exchange
    logIndex
    maker
    price
    quoteCurrency
    side
    taker
    thumbnailUrl
    timestamp
    tokenId
    tx
    txIndex

          }
        }
        ''')
    tr=pd.DataFrame(client.execute(query)['nftTrades'])    
    return tr


def pull_data_api(client,tr):
    trs=[]
    while True:
        before = tr['timestamp'].min()
        print(before)
        query = gql('''
    { 
        nftTrades(limit:1000,since:1649804649, collectionName:"Parallel Alpha", before:''' + str(before) + ''') {
        chain
        collectionAddress
        collectionName
        exchange
        logIndex
        maker
        price
        quoteCurrency
        side
        taker
        thumbnailUrl
        timestamp
        tokenId
        tx
        txIndex

            }
        }
        ''')
        while True:
            try:
                ex = client.execute(query)
                break
            except:
                print ('retrying')
                pass
        tr = pd.DataFrame(ex['nftTrades'])
        print (tr.shape)
        tr.to_csv(str(before)+'.csv')
        trs.append(tr)
        
    
    
if __name__ == '__main__':
    client = get_connection('https://api.parsec.finance/api/v2',{'api_key':'API_KEY'})
    tr=fetch_initial_data()
    pull_data_api(client,tr)

