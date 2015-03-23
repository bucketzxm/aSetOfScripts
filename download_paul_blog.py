#!/bin/python3
'''
	抓去 paul 的博客所有博客 (因为我想打印着看orz)
'''
import requests
from bs4 import BeautifulSoup 

base_url = "http://www.paulgraham.com/"

page_que = []

def get_index(url):
	res = requests.get(url)
	soup = BeautifulSoup( res.text)
	tag = soup.find_all('a')
	print(tag)


def feed_url():
	pass

if __name__ == "__main__":
	
	get_index( base_url+'ind.html')
