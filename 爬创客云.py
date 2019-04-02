# import requests
# from bs4 import BeautifulSoup
# import time		
# import asyncio
# from pyppeteer import launch
# headers = {
# 	'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
# 	}
# a = set()
# cc = set()
# # url='https://www.22vd.com/'    #https://www.22vd.com/go?url=http://artemis.va666.com/
# url_list=[]
# def url_jh(url):
# 	r =requests.get(url,headers = headers,timeout = 20)
# 	soup = BeautifulSoup(r.text,'lxml')
# 	u_list=soup.find_all('a')
# 	for i in u_list:
# 		set1 = i.get('href')
# 		if set1== None:
# 			continue
# 		elif set1.split('//')[0].strip() =='/go?url=http:':
# 			set1 = 'https://www.22vd.com/'+set1.lstrip('/')
# 			print(set1)
# 			cc.add(set1)
# 		elif set1.split('//')[0].strip() !='https:' and set1.split('//')[0].strip() !='http:':
# 			# print(set1)
# 			set1 = 'https://www.22vd.com/'+set1.lstrip('/')
# 			a.add(set1)
# 		else:
# 			a.add(set1)
		
# url_jh(url='https://www.22vd.com/')

# if __name__ == '__main__':
# 	b=a.copy()
# 	for i in b:
# 		url_jh(url=i)
# 	print(cc)

q = {'https://www.22vd.com/go?url=http://demoplazathemes.com/wordpress/oganidemo/', 'https://www.22vd.com/go?url=http://rometheme.net/html/gaco/', 'https://www.22vd.com/go?url=http://cloud_126.va666.com/', 'https://www.22vd.com/go?url=http://nouthemes.com/magento/thelook/demo/', 'https://www.22vd.com/go?url=http://theme-sphere.com/demo/smart-mag-landing/', 'https://www.22vd.com/go?url=http://www.sj520.cn/', 'https://www.22vd.com/go?url=http://themes.artivity.co.uk/basix/', 'https://www.22vd.com/go?url=http://artemistheme.com/themepreview/', 'https://www.22vd.com/go?url=http://demo.roadthemes.com/junko/', 'https://www.22vd.com/go?url=http://www.klobouckalesni.cz/en/', 'https://www.22vd.com/go?url=http://ss2017.descente.jp/', 'https://www.22vd.com/go?url=http://en.uglerod.ru/', 'https://www.22vd.com/go?url=http://cloud_129.va666.com/', 'https://www.22vd.com/go?url=http://94photography.com/', 'https://www.22vd.com/go?url=http://demo.roadthemes.com/artfurniture/', 'https://www.22vd.com/go?url=http://themes.potenzaglobalsolutions.com/html/seohub-seo-marketing-social-media-multipurpose-html5-template/', 'https://www.22vd.com/go?url=http://www.d.commonsupport.com/rexal/', 'https://www.22vd.com/go?url=http://ninethemes.net/epro/opencart/', 'https://www.22vd.com/go?url=http://glacier.mountaintheme.com/', 'https://www.22vd.com/go?url=http://www.symansbon.cn/', 'https://www.22vd.com/go?url=http://demo.mesathemes.com/', 'https://www.22vd.com/go?url=http://atomlab.thememove.com/', 'https://www.22vd.com/go?url=http://cloud_123.va666.com/', 'https://www.22vd.com/go?url=http://helas.la-studioweb.com/landing/', 'https://www.22vd.com/go?url=http://killingofasacreddeer.movie/', 'https://www.22vd.com/go?url=http://www.pixelmotionfilms.com/', 'https://www.22vd.com/go?url=http://kolaps.com/en/', 'https://www.22vd.com/go?url=http://magento2.flytheme.net/themes/sm_market2/intro/index.html', 'https://www.22vd.com/go?url=http://www.fluidmedia.gr', 'https://www.22vd.com/go?url=http://www.bluecloudventures.com/', 'https://www.22vd.com/go?url=http://cloud_122.va666.com/', 'https://www.22vd.com/go?url=http://cloud_117.va666.com/', 'https://www.22vd.com/go?url=http://cloud_59.va666.com/', 'https://www.22vd.com/go?url=http://artfurniture.va666.com/', 'https://www.22vd.com/go?url=http://themes.framework-y.com/fullpage/', 'https://www.22vd.com/go?url=http://demo.roadthemes.com/belly/', 'https://www.22vd.com/go?url=http://clorova.com/', 'https://www.22vd.com/go?url=http://www.apploud.cz/', 'https://www.22vd.com/go?url=http://roarkstudio.pl/', 'https://www.22vd.com/go?url=http://basix.va666.com/'}
print(len(q))