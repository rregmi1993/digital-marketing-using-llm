import tweepy
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

# twitter = tweepy.Client(
#     config['DEFAULT']['API_KEY'],
#     config['DEFAULT']['API_SECRET'],
#     config['DEFAULT']['access_token'],
#     config['DEFAULT']['access_token_secret']
# )

# response = twitter.create_tweet(text='hello world')
# print("Hello world !!!")

# API keyws that yous saved earlier
api_key = config['DEFAULT']['API_KEY']
api_secrets = config['DEFAULT']['API_SECRET']
access_token = config['DEFAULT']['access_token']
access_secret = config['DEFAULT']['access_token_secret']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')
    status = "This is my first post to Twitter using the API. I am still learning, please be kind :)"
    api.update_status(status=status)
except Exception as e:
    print('Failed authentication' + str(e))