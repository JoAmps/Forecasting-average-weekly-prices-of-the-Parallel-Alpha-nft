#import the neccesary libraries
import psycopg2
import pandas as pd
import snscrape.modules.twitter as sntwitter


def connect(Db_host,Db_name,Db_user,Db_pass):
    conn = psycopg2.connect(host=Db_host, dbname=Db_name, user=Db_user,password=Db_pass)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    return cur,conn

def obtain_data():
    tweets_list = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper("Parallel Alpha since:2021-08-01 until:2022-08-09").get_items()):
        if i>1000:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.username,tweet.retweetCount,tweet.likeCount,tweet.quotedTweet])
    df=pd.DataFrame(tweets_list, columns=['date','tweet_id','tweet','username','retweets','likes','quotes']) 
    return df

def create_table(df,cur):
    df["id"] = df.index + 1
    cur.execute("CREATE TABLE parallel_alpha_tweet (date date, tweet_id bigint,\
        tweet varchar, username varchar, retweets int,likes int, id int PRIMARY KEY);")

def insert_to_database(cur,df,conn):
    insert_tweets="""
    INSERT INTO parallel_alpha_tweet(date,tweet_id,tweet,username,retweets,likes,id)
    VALUES(%s,%s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO UPDATE SET(date,tweet_id,tweet,username,retweets,likes)=(EXCLUDED.date,\
        EXCLUDED.tweet_id,EXCLUDED.tweet,EXCLUDED.username,\
    EXCLUDED.retweets,EXCLUDED.likes)
    """
    for _, row in df.iterrows():
        cur.execute(insert_tweets, row.values.tolist())
        conn.commit()

if __name__ == '__main__':
    cur,conn=connect(Db_host='host_name', Db_name='database_name' ,Db_user='user_name', Db_pass='password')
    df=obtain_data() 
    create_table(df,cur)
    insert_to_database(cur,df,conn)

