# crypto-price-tracker

Example: https://twitter.com/polygontracker
<h2>Why Did You Make It?</h2>
I did it primarily as a side-project/ complement to a larger website which tracks Polygon/ gives information on the coin.

<h2>What Does It Do?</h2>
It is a Twitter bot to track hourly price change of any crypto utilizing twitter developer portal, CoinMarketCap API endpoints, and tweepy python library.

<h2>How Do You Use It?</h2>
1. You need to set up an account on https://developer.twitter.com/ this will give you access to your keys which you need to access endpoints. <br></br>
2. Apply for elevated access; this is needed to use the tweepy library. <br></br>
3. Email them back and forth for two days, essentially, you're telling them what you're doing and why you want access. <br></br>
4. Set up an account on https://coinmarketcap.com/api/ and get your API key there. <br></br>
5. Plug & play. There are variables in credentials.py where you will update the keys appropriately, as well in main.py where you will update the coin symbol & name.<br></br>

###<h2>Things I plan on Adding</h2>
- [ ] Migrate/ Utilize CoinGecko API endpoints instead of CoinMarketCap (way more flexible, and allows for more requests)
- [ ] Reply feature to tell you current price
- [ ] Price jump alerts (5-10% leap in 10 minute span)

