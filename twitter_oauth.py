from tweepy import OAuthHandler

access_token = "99197787-uPgIm4C4gWG4CF9vsiy20sTjXGwLJrfKFd8G2y7kC"
access_token_secret = "cDDmod0zLEGiY08G66tmjcxJnH8focPqjP7Fy85nhMJXy"
consumer_key = "XxehyK6h9z5U3WBnDAeZjJmSi"
consumer_secret = "oW601OmuJHCVjyWqPuGePDgxj1ZMiTAYL2msNqESTvlTLsWDNE"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
