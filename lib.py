#coding=utf-8
import urllib, urllib2, sys, json, os, shutil
from prettytable import PrettyTable

def getweather(appcode,city):
    host = 'http://jisutqybmf.market.alicloudapi.com'
    path = '/weather/query'
    method = 'GET'
    querys = 'city=' + city
    bodys = {}
    url = host + path + '?' + querys

    request = urllib2.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urllib2.urlopen(request)
    content = response.read()
    return content;
