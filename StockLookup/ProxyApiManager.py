"""
    Manage your proxy api urls very easily
"""

import random

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
        