import cPickle as pickle
import json
import os
import codecs

from db_related import user_tweets_db
from json_related import get_json_item
from json_related import timestamp_to_date


# Constants

if __name__ == '__main__':
    if os.path.exists('result'):
        pass
    else:
        os.mkdir('result')

    try:
        for (user_id, raw_contents) in user_tweets_db.iterator():
            json_contents_list = pickle.loads(raw_contents)
            filename = 'result/%s.csv' % user_id
            fid = codecs.open(filename, encoding='utf-8', mode='w')
            for tweet in json_contents_list:
                tweet_id = get_json_item(tweet, [u'id_str'])
                time = get_json_item(tweet, [u'created_at'])
                text = get_json_item(tweet, [u'text']).replace(',','.')
                coord = get_json_item(tweet, [u'coordinates', u'coordinates'])
                if coord is not None:
                    coord = ';'.join(map(str, coord))
                place = get_json_item(tweet, [u'place', u'full_name'])
                # text = ''.join(get_json_item(tweet, [u'text']).split())
                to_put = [user_id, tweet_id, time, text, coord, place]
                to_write = '\t'.join([x.replace(',', '.').replace('\n','.') for x in to_put]) + '\n'
                fid.write(to_write)
            fid.close()
            
    except KeyboardInterrupt:
        print(' Ended')
