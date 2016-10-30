import plyvel

tweets_db = plyvel.DB('./DBS/tweets_db.ldb', create_if_missing=True)
userid_db = plyvel.DB('./DBS/userid_db.ldb', create_if_missing=True)
user_tweets_db = plyvel.DB('./DBS/user_tweets_db.ldb', create_if_missing=True)

