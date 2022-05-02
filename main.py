import tweepy
import json
from requests import Session
import time
import credentials

# Using matic/polygon as an example...
symbol = 'MATIC' # change to appropriate symbol
name = 'Polygon'

def generate_data(old_price):
    """
    Pulls current data for coin from coinmarketcap API endpoint
    """
    # keys and params for coinmarketcap
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    cmc_key = credentials.CMC_API_key
    
    parameters = {
      'symbol' : symbol,
      'convert' : 'USD',
    }
  
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': cmc_key,
    }
  
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    curr_price = float(
      json.loads(response.text)['data']['MATIC'][0]['quote']['USD']['price']
    )
    percent_change = ((curr_price-old_price)/old_price)*100
    print("Price collection OK.")
    return (curr_price, percent_change)


def tweet_price(CMC_data, count):
    """
    Take current price and percent change data and tweets it.
    """
    # keys for twitter
    consumer_key = credentials.API_key
    consumer_secret = credentials.API_secret_key
    access_token = credentials.access_token
    access_token_secret = credentials.access_token_secret
  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
  
    try:
        api.verify_credentials()
        print("Authentication OK.")
    except:
        print("Error during authentication")
  
    # increase tweet count, truncate & define data
    current_price = round(CMC_data[0], 3)
    percent_change = round(CMC_data[1], 3)
    # Create a tweet
    api.update_status(
      f"{name}'s price is ${current_price}, a percent change of \
      {percent_change}% from an hour ago. Tweet Count: {count}"
    )


def run():
  """
  Run the twitter bot.
  """
  # get old price
  count = 0
  hour = 60*60
  initial_run = generate_data(1)
  price = initial_run[0]
  while True:
      time.sleep(hour)
      count += 1
      new = generate_data(price)
      price = new[0]
      tweet_price(new, count)


if __name__ == '__main__':
  run()
