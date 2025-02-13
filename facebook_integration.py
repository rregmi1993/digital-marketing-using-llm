import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv()
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')


# FACEBOOK_HOSTNAME = os.environ.get("HOSTNAME", "graph.facebook.com")
FACEBOOK_API = "https://" +  "graph.facebook.com" + "/v14.0"
FACEBOOK_ACCESS_TOKEN = config['DEFAULT']['FACEBOOK_ACCESS_TOKEN']
FACEBOOK_PAGE_ID =config['DEFAULT']["FACEBOOK_PAGE_ID"]

#Your Access Keys
def post_in_facebook(message):
    

    post_url = 'https://graph.facebook.com/{}/feed'.format(FACEBOOK_PAGE_ID)
    payload = {
        'message': message,
        'access_token': FACEBOOK_ACCESS_TOKEN
        }
    r = requests.post(post_url, data=payload)
    # print(r.text)
    return r.text