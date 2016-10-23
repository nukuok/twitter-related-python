import cPickle as pickle
import json

from tweepy.streaming import StreamListener
from tweepy import Stream

from bounding_box import bb_japan
from bounding_box import bb_tokyo_p
from bounding_box import bb_tokyo
from bounding_box import bb_NY
from db_related import tweets_db
from json_related import get_json_item
from json_related import extract_ymd
from twitter_oauth import auth

# Constants

SEARCH_REGION = bb_tokyo_p

count = 0

class StdOutListener(StreamListener):
    def on_data(self, data):
        global count
        # print type(data)
        tweet = json.loads(data)
        tweet_id = get_json_item(tweet, ['id_str']).encode()
        if tweets_db.get(tweet_id):
            pass
        else:
            lang = get_json_item(tweet, ['lang']).encode()
            if lang != 'ja':
                tweets_db.put(tweet_id, pickle.dumps(tweet))
                print("Put tweet %s to db." % tweet_id)
                count += 1
            else:
                print('Skipped Japanese tweet')
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    try:
        l = StdOutListener()
        stream = Stream(auth, l)

        stream.filter(locations=bb_tokyo_p)
    except KeyboardInterrupt:
        print(' Ended')
        print('%d tweets stored.' % count)

