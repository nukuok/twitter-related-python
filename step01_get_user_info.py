import cPickle as pickle
import json

import tweepy

from db_related import tweets_db
from db_related import userid_db
from json_related import get_json_item
from twitter_oauth import auth

# Constants

if __name__ == '__main__':
    api = tweepy.API(auth)
    
    try:
        tweet_list = tweets_db.iterator()
        for (tweet_id, raw_contents) in tweet_list:
            json_contents = pickle.loads(raw_contents)
            user_id = get_json_item(json_contents, [u'user', u'id_str'])
            
            if userid_db.get(user_id.encode()):
                print('User info exists.')
            else:
                user = api.get_user('twitter')
                json_info = user._json
                userid_db.put(user_id.encode(), pickle.dumps(json_info))
                print('User %s info stored.' % user_id.encode())
                
    except KeyboardInterrupt:
        print(' Ended')
