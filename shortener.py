#import requests
#from bs4 import BeautifulSoup
#def short_url(url):
#    api = 'https://shortest.link/es/'
#    resp = requests.post(api,data={'url':url})
#    if resp.status_code == 200:
#        soup = BeautifulSoup(resp.text,'html.parser')
#        shorten = soup.find('input',{'class':'short-url'})['value']
#        return shorten
#    return url
import requests
import json

def short_url(url):
    requrl = 'https://xd-core-api.onrender.com/xdlinks/encode'
    jsondata = {"channelId":"","urls":urls}
    headers = {"Content-type":"application/json"}
    resp = requests.post(requrl,data=json.dumps(jsondata),headers=headers)
    return parsejson(resp.text)

def parsejson(json):
        data = {}
        tokens = str(json).replace('{','').replace('}','').split(',')
        for t in tokens:
            split = str(t).split(':',1)
            data[str(split[0]).replace('"','')] = str(split[1]).replace('"','')
        return data['data']