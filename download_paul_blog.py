#!/bin/python3
'''
	抓去 paul 的博客所有博客 (因为我想打印着看orz)
'''
import queue
import requests
import time
from bs4 import BeautifulSoup 

base_url = "http://www.paulgraham.com/"

page_que = queue.Queue() 

def get_index(url):
	res = requests.get(url)
	soup = BeautifulSoup( res.text)
	tag = soup.find_all('a')
	for page in tag:
		print(page.contents)
		if page.contents[0] == 'Next':
			page_que.put(base_url+page['href'])
		elif page.contents[0] == 'Prev':
			pass
		else:
			feed_url( page['href'] ,page.contents[0])

def feed_url(url,page_name):
	page_name = str(page_name)
	if "/" in page_name:
		page_name = page_name.replace('/',' ')
	print( "downloading "+url+ " " + str(page_name))
	if url == "index.html":
		pass
	else:
		res = requests.get(base_url+url)
		with open('/tmp/paul/'+page_name+'.html','w') as f:
			f.write( res.text)

if __name__ == "__main__":
	begin_time = time.clock()
	page_que.put(base_url+'ind.html')	
	while not page_que.empty():
		st = page_que.get()
		print("now we are in the page of " + st)
		get_index( st )
	end_time = time.clock()

	print( "Total cost time : " +str( end_time - begin_time))
