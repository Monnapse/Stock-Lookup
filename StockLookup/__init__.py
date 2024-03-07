"""
    StockLookup
    Made by Monnapse
    Lookup stock info using yahoo finance
"""

import requests
import time
import random

wait_time = 20

# PAM Package
class NewProxyApi:
    def __init__(self, name) -> None:
        self.name = name
        
        self.base_urls = []
        self.subs = {}
    def __str__(self) -> str:
        return self.name
    def add_base(self, url) -> None:
        self.base_urls.append(url)
    def add_base_urls(self, urls: list):
        for i in urls:
            self.add_base(i)
    def get_base_url(self) -> str:
        return self.base_urls[random.randint(0, len(self.base_urls)-1)]
    def add_sub(self, name: str):
        if self.subs.get(name):
            # Already exists
            return None
        else:
            self.subs[name] = []
    def add_sub_url(self, sub_name: str, url: str):
        
        self.subs[sub_name].append(url)

        
    def add_sub_urls(self, sub_name: str, urls: list):
        
        for i in urls:
            self.add_sub_url(sub_name, i)
        
    def get_sub_url(self, sub_name):
        
        return self.subs[sub_name][random.randint(0, len(self.subs[sub_name])-1)]
        
    def get_full_url(self, sub_name):
        return self.get_base_url()+self.get_sub_url(sub_name)

lookup_sub = "stock_lookup"

yahoo_proxy = NewProxyApi("yahoo")
yahoo_proxy.add_base_urls([
    "https://query1.finance.yahoo.com", "https://query2.finance.yahoo.com"
])
yahoo_proxy.add_sub(lookup_sub)
yahoo_proxy.add_sub_url(lookup_sub, "/v8/finance/chart/{symbol}?period1={timestamp}&period2={timestamp}")

def get_stock(symbol):
    """
        Gets just the basic info about the stock
    """

    # request
    timestamp = int(time.time())
    
    url = yahoo_proxy.get_full_url(lookup_sub).format(symbol=symbol, timestamp=timestamp)
    
    headers = {
        "User-Agent": "curl/7.68.0"
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()

    if response_json == None or response_json == 'NoneType': return None
    
    result = response_json["chart"]["result"]
    
    if result == None: return

    data = result[0]["meta"]
    return {
        "market_price":  data["regularMarketPrice"],
        "currency": data["currency"],
        "exchange_name": data["exchangeName"],
    }