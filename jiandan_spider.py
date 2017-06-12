# -*- coding:utf-8 -*-
'''
version:Python 2.6
standard libs:urllib
author:Dead_morning
system: cetos 6.5
'''
import re
import urllib


def get_content(html_page):
	'''html downladd'''
	html = urllib.urlopen(html_page)
	content = html.read()
	html.close()

	return content


def get_images(info):
	'''html parser'''
	regex = r'href="//wx(.+?\.(?:gif|jpg|jpeg|png))" ' # download original picture
	pat = re.compile(regex)
	image_code = map(lambda x: 'http://wx'+ x , re.findall(pat,info))
	return image_code

def Download_image():
	''' image download'''
	for image_url in get_images(info):
		print image_url
		image_name = image_url.split('/')[-1]
	
		urllib.urlretrieve(image_url,image_name)


def html_pages():
	''' URl list'''
	b = []
	for a in range (1 ,95):
		url= 'http://jandan.net/ooxx/page-%s#comments' %a
		b.append(url)
	return b 


if __name__ == '__main__':

	for html_page in html_pages():
		info = get_content(html_page)
		print Download_image()

	


	

	