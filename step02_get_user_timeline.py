import cPickle as pickle
import json

import tweepy

from db_related import userid_db
from db_related import user_tweets_db
from json_related import get_json_item
from twitter_oauth import auth

# Constants

if __name__ == '__main__':
    api = tweepy.API(auth)
    
    try:
        user_list = userid_db.iterator()
        for (user_id, _) in user_list:
            tweet_list = api.user_timeline(int(user_id), count = 20)
            json_contents = [tweet._json for tweet in tweet_list]
            
            if user_tweets_db.get(user_id.encode()):
                print('User tweets exists.')
            else:
                user_tweets_db.put(user_id.encode(), pickle.dumps(json_contents))
                print('User %s tweets stored.' % user_id.encode())

                
    except KeyboardInterrupt:
        print(' Ended')
