import urllib.request
from bs4 import BeautifulSoup
import re
import os
import textwrap
 
news_title = []
news_body = []
news_time = []
news_loc = []

url="http://www.bbc.com/news"
htmlfile=urllib.request.urlopen(url)
soup=BeautifulSoup(htmlfile,"html.parser")

news_title_soup=soup.findAll(class_="gs-c-promo-heading nw-o-link-split__anchor gs-o-faux-block-link__overlay-link gel-pica-bold")
news_body_soup=soup.findAll(class_="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")
news_time_soup=soup.findAll(class_="qa-status-date-output")
news_loc_soup=soup.findAll(class_="gs-c-section-link gs-c-section-link--truncate nw-c-section-link nw-o-link nw-o-link--no-visited-state")

for post in range(0,10):
	news_title.append(news_title_soup[post].get_text())
	news_body.append(news_body_soup[post].get_text())
	news_time.append(news_time_soup[post].get_text())
	news_loc.append(news_loc_soup[post].get_text())

file = open('file.txt','w')
for postout in range(0,5):
	print("\n"+str(postout+1)+">"+news_title[postout])
	file.write("\n"+str(postout+1)+">"+news_title[postout]+"\n")

	print("---------------------------")	
	file.write("---------------------------\n")	

	print(textwrap.fill(news_body[postout], 40))
	file.write(textwrap.fill(news_body[postout], 40)+"\n")

	print("---------------------------")	
	file.write("---------------------------\n")	
	
	print("Source Details:"+news_time[postout]+" ago from "+news_loc[postout])
	file.write("Source Details:"+news_time[postout]+" ago from "+news_loc[postout]+"\n")
file.close()
#a = soup1.replace('\n','')

import http.client
file = open('file.txt', 'r')
news = file.read()
file.close()

soup1 = news.replace("\n","%0A")
soup2 = soup1.replace(" ","%20")
soup3 = soup2.replace("&","and")
print("\n\n\n"+soup3)

to_number="919992854050"
from_number="12313665106"
payloaddata = "To=%2B"+to_number+"&From=%2B"+from_number+"&Body=Headlines"+"%0A%0A"+soup3

conn = http.client.HTTPSConnection("api.twilio.com")
payload = payloaddata #"To=%2B919992854050&From=%2B12313665106&Body=API%20Call%20Successful"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'authorization': "Basic QUNkOTYzNTAwNzg2Mzg2N2E0ZDcyYjllYzZiMzg3NTkzMTo2MTFmNDg4ODBjZmJmNzE5YTk0NWRjMTY3M2YyY2RlMQ==",
    'cache-control': "no-cache",
    'postman-token': "712e25f7-f599-d22f-023b-5d3e746e9a39"
    }

conn.request("POST", "/2010-04-01/Accounts/ACd9635007863867a4d72b9ec6b3875931/Messages.json", payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))