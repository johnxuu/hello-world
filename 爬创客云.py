import requests
from bs4 import BeautifulSoup
import time		
import asyncio
from pyppeteer import launch
headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
	}
a = set()
cc = set()
# url='https://www.22vd.com/'    #https://www.22vd.com/go?url=http://artemis.va666.com/
url_list=[]
def url_jh(url):
	r =requests.get(url,headers = headers,timeout = 20)
	soup = BeautifulSoup(r.text,'lxml')
	u_list=soup.find_all('a')
	for i in u_list:
		set1 = i.get('href')
		if set1== None:
			continue
		elif set1.split('//')[0].strip() =='/go?url=http:':
			set1 = 'https://www.22vd.com/'+set1.lstrip('/')
			# print(set1)
			cc.add(set1)
		elif set1.split('//')[0].strip() !='https:' and set1.split('//')[0].strip() !='http:':
			# print(set1)
			set1 = 'https://www.22vd.com/'+set1.lstrip('/')
			a.add(set1)
		else:
			a.add(set1)
		
url_jh(url='https://www.22vd.com/')

if __name__ == '__main__':
	b=a.copy()
	for i in b:
		url_jh(url=i)
	print(cc)

