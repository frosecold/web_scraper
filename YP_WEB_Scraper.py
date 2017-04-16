#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:13:24 2017

@author: franco
"""

import requests
from bs4 import BeautifulSoup

#url = "https://www.yellowpages.com/search?search_terms=restaurant&geo_location_terms=Miami%2C+FL"
#url = "https://www.yellowpages.com/search?search_terms=car+dealership&geo_location_terms=Miami%2C+FL"
url= "https://www.yellowpages.com/search?search_terms=Dog+Day+Care&geo_location_terms=Miami%2C+FL"
r = requests.get(url)

soup = BeautifulSoup(r.content)

#links = soup.find_all("a") # Con esto guardamos en links todos los links en la pagina identificados con el <a>

#for link in links:
    #Z= link.get("href")
    #Y= link.text
    #print(Z)
    #print(type(Z))
    #try:
        #if "http" in Z:
            #print(Z+' '+Y)
    #except BaseException as e:
        #pass
        #print("NONE")
        
g_data = soup.find_all("div", {"class": "info"})
for item in g_data:
    try:
        print('Company Name: '+ item.contents[0].find_all("a", {"class": "business-name"})[0].text)
    except:
        pass
    try:
        A=item.contents[1].find_all("p", {"class": "adr"})[0].text
        address=A.split(',')[0]
        zipc=A.split('FL')[1]
        state=A.split(', FL')[0].split(',')[1]
        print('Locality: '+state)
        print('Address: ' + address)
        print('ZIP: ' + zipc)
    except:
        pass
    try:
        print('Phone: ' + item.contents[1].find_all("li", {"class": "phone primary"})[0].text)
    except:
        print('NO PHONE')