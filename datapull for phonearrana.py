# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 22:09:24 2020

data pull from phonearrana

@author: Siddy
"""
print("starting......")
from bs4 import BeautifulSoup
import requests
import urllib
import pandas as pd

device=list()
date=list()
display=list()
camera=list()
storage=list()
ram=list()
price=list()
battery=list()
operating_system=list()
url=list()


def find_all_page_links(Url,pagelinks):
    try:
    
        htmlContent = urllib.request.urlopen(Url).read()
        soup=BeautifulSoup(htmlContent,'html.parser') 
        nav=soup.find('nav',attrs={'aria-label':'navigation'})
        links=nav.find_all('a')
        
        for link in links:
            if(link.get('href')!='#'):
                pagelinks.append(link.get('href'))
    
    except:
        print("error in find all page links")
def get_device_data(Url):
    try:
        print(Url)
        htmlContent = urllib.request.urlopen(Url).read()
        soup=BeautifulSoup(htmlContent,'html.parser')
        #dev=soup.find('li',attrs={'class':'active'}).text
        
        div_data=soup.find('section',attrs={'class':'phone__section phone__section_widget_quickSpecs'})
        if div_data != None:
            links=div_data.find_all('a')
            dev=soup.find('li',attrs={'class':'active'}).text
            dat=""
            dis=""
            cam=""
            ra=""
            sto=""
            bat=""
            os=""
            pr=""
            
            
    
    
            '''
            if len(links)>=5:
    
                dat=links[0].find('p').text
                if 'Mp' in links[2].find('p').text.replace('\n',' '):
                    cam=links[2].find('p').text.replace('\n',' ')
                if 'Ram' in links[3].find('p').text.replace('\n',' '):
                    ra=links[3].find('p').text.replace('\n',' ')
                if 'GB' in  links[4].find('p').text.replace('\n',' '):
                    sto=links[4].find('p').text.replace('\n',' ')
                    
                    
                tbody_data=soup.find_all('tbody')
    
                j=0
                for data in tbody_data:
    
                    if 'Differences from the main variant:' not in data.text and 'Price' in data.text:
                        pr=data.text.replace('\n',' ')
                    elif 'Differences from the main variant:' in data.text:
                        alt.append(data.text.replace('\n',' '))
    
             '''
            for li in links:
                temp=li.text.replace('\n','')
                if "Released" in temp:
                    dat=li.find('p').text.replace('\n','')
                elif "Display" in temp:
                    dis=li.find('p').text.replace('\n','')
                elif "Camera" in temp:
                    cam=li.find('p').text.replace('\n','')
                elif "Hardware" in temp:
                    ra=li.find('p').text.replace('\n','')
                elif "Storage" in temp:
                    sto=li.find('p').text.replace('\n','')
                elif "Battery" in temp:
                    bat=li.find('p').text.replace('\n','')
                elif "OS" in temp:
                    op=li.find('p').text.replace('\n','')
                    
            
            '''
            te=soup.find_all('section',attrs={'class':"page__section page__section_specs"})
            for t in te:
                if 'Buyers information' in  t.text and 'Price' in t.text:
                    tb=t.find_all('tbody')
                    for tbb in tb:
                        if "Price" in tbb.text:
                            pr=tbb.text
            '''
            te=soup.find_all('table')
            for t in te:
                 if 'Buyers information' in  t.text and 'Price' in t.text:    
                         pr=t.text
                            
                            
            device.append(dev)               
            date.append(dat)
            display.append(dis)
            camera.append(cam)
            ram.append(ra)
            storage.append(sto)
            battery.append(bat)
            price.append(pr)
            operating_system.append(os)
            url.append(Url)
            
            
            at=soup.find_all('div',attrs={'class':"widgetAlternativeVariants"})
            for a in at:
                dev=""
                
                dis=""
                cam=""
                ra=""
                sto=""
                bat=""
                
                pr=""
               
                dev=a.find('header').text.replace('\n','')
                print(dev)
                tb=a.find_all('td')
                for i in tb:
                    print(i.text)
                    if 'GB' in i.text:
                        sto=i.text.replace('\n','')
                    if '$' in i.text:
                        pr=i.text.replace('\n','')
                    
                device.append(dev)               
                date.append(dat)
                display.append(dis)
                camera.append(cam)
                ram.append(ra)
                storage.append(sto)
                battery.append(bat)
                
                price.append(pr)
                operating_system.append(os)
                url.append(Url)    
    except:
        print("error in get device data")

def find_all_device_links(Url):
    try:
        htmlContent = urllib.request.urlopen(Url).read()
        soup=BeautifulSoup(htmlContent,'html.parser') 
        div_data=soup.find('div',attrs={'class':'stream block'})
        links=div_data.find_all('a')
        device_links=set()
        for link in links:
            if(link.get('href')!='#'):
                device_links.add(link.get('href'))
        return device_links
    except:
        print("error")
        
        return '#'

Url="https://www.phonearena.com/phones/manufacturers/lg"
visitedlinks=set()
pagelinks=list()

pagelinks.append(Url)
for link in pagelinks: 
    Url=link
    if link not in visitedlinks and link !='#':             
        
        device_links=find_all_device_links(link)
        print(device_links)
        for li in device_links:
            if li not in visitedlinks and li!='#':
                
                get_device_data(li)
                visitedlinks.add(li)
        
        find_all_page_links(link,pagelinks)
        visitedlinks.add(link)
len(visitedlinks)

df=pd.DataFrame()
df['device']=device
df['date']=date
df['camera']=camera
df['storage']=storage
df['ram']=ram
df['price']=price
df['url']=url
df['battery']=battery
df['display']=display
df['os']=operating_system


df.to_excel("lg data from phonearrana5.xlsx")