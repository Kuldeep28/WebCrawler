#!/ usr / bin / env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 00:09:49 2019

@author: kuldeep
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re
import http

# connection to mak a connectioe btwen code  and the processor
conn = pymysql.connect(host='127.0.0.1', unix_socket='/var/run/mysqld/mysqld.sock', user='root', passwd='Kido@1728',
                       db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute("USE enno")

random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute("INSERT INTO peges (title, content) VALUES (\"%s\",\"%s\")", (title, content))
    cur.connection.commit()


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html)
    try:
        title = bsObj.find("h1").get_text()
    except AttributeError as e:
        print(e)
        title = "notfound"
    content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
try:
    html_page = urlopen("https://www.goodreads.com/genres/most_read/business")
    print(type(html_page))
    bsObj = BeautifulSoup(html_page)
    li1x = list([a.find("script") for a in bsObj.find_all("div", {"class": "leftAlignedImage bookBox"})])
    li2x = list([a.find("a") for a in bsObj.find_all("div", {"class": "leftAlignedImage bookBox"})])
    bs_script_obj = list()
    useful_list = list()
    front_index = 0;
    for element in li1x:
        element = __builtins__.str(element)
        # if(!(int(element.find("<h2><a class"))==-1) and !(int(element.find('On: false, w5 });'))==-1)):
        element = element[
                  int(element.find("<h2><a class")):int(element.find(" { style: 'addbook', stem: 'leftMiddle'"))]
        element = "<html><head></head><body>" + element + "</body></html>"
        element = element.replace("\n", "")
        element = element.replace("\n\n", "")
        element = element.replace("\\", "")
        element = element.replace("/", "")
        element = element.replace(" n ", "")
        element = element.replace(" nn ", "")
        element = element.replace(" nnn ", "")
        bs_script_obj.append(element)
        front_index < -element.find("<div class=\"addBookTipDescription\">")
        front_index = front_index + 54 + 15
        bottom_index = element.find(" href=\"#\" onclick=\"swapContent($(this));; return false;\">..")
        bottom_index = bottom_index - 50
        useful_list.append(element[front_index:bottom_index] + "\n" + "====================")
    print("=====================================================")
    print()
    # print(li2x[0])
    print()
    print("===============printing useful=========================")
    i = 1
    for useful_listq in useful_list:
        print(i)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(useful_listq)
        i = i + 1
        print(li1x[23].next_element)
#todo: use regular expression to get data from the script tag
finally:
    cur.close()
    conn.close()

