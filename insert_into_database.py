import psycopg2
import pandas as pd


def connect(Db_host,Db_name,Db_user,Db_pass):
    conn = psycopg2.connect(host=Db_host, dbname=Db_name, user=Db_user,password=Db_pass)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    return cur,conn

def import_data(path):
    df=pd.read_csv(path)
    df=df.drop(columns='Unnamed: 0')
    return df

def create_table(df,cur):
    df["id"] = df.index + 1
    cur.execute("CREATE TABLE parallel_alpha_trades (chain varchar, collectionAddress varchar,\
        collectionName varchar, exchange varchar, logIndex int,maker varchar, price float,\
        quoteCurrency varchar, side varchar, taker varchar, thumbnailUrl varchar, timestamp int,\
        tokenId float, tx varchar, txIndex float, id int PRIMARY KEY);")

def insert_to_database(cur,df,conn):
    insert_trades="""
    INSERT INTO parallel_alpha_trades(chain,collectionAddress,collectionName,exchange,logIndex,maker,price,\
    quoteCurrency,side,taker,thumbnailUrl,timestamp,tokenId,tx,txIndex,id)
    VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s, %s, %s, %s, %s)
    ON CONFLICT (id) DO UPDATE SET(chain,collectionAddress,collectionName,exchange,logIndex,maker,price,\
    quoteCurrency,side,taker,thumbnailUrl,timestamp,tokenId,tx,txIndex)=(EXCLUDED.chain,\
        EXCLUDED.collectionAddress,EXCLUDED.collectionName,EXCLUDED.exchange,\
    EXCLUDED.logIndex,EXCLUDED.maker,EXCLUDED.price,EXCLUDED.quoteCurrency,EXCLUDED.side,\
        EXCLUDED.taker,EXCLUDED.thumbnailUrl,EXCLUDED.timestamp,EXCLUDED.tokenId,\
    EXCLUDED.tx,EXCLUDED.txIndex)
    """
    for i, row in df.iterrows():
        cur.execute(insert_trades, row.values.tolist())
        conn.commit()

if __name__ == '__main__':
    cur,conn=connect(Db_host='host_name', Db_name='database_name' ,Db_user='user_name', Db_pass='password')
    df=import_data('data/parallel_alpha_raw_data.csv') 
    create_table(df,cur)
    insert_to_database(cur,df,conn)

