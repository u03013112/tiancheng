# encoding:utf-8
import requests
import json

class Spider:
    def __init__(self):
        self.url = 'http://s6206ws.shangxiangfushi.com/api/public/?service=Home.getHot'
    def sp(self):
        self.data = []
        for p in range(1,10):
            try:
                data = {'p':(None,p)}
                headers = {'User-Agent': 'fuxk u'}
                r = requests.request("POST",self.url,files=data,headers=headers,timeout=10)
                data = r.json()['data']['info'][0]['list']
                if len(data) == 0:
                    break
                for d in data:
                    self.data.append(d)
            except Exception as e:
                print(e)
        return None

if __name__=='__main__':  
    s = Spider()
    s.sp()
    print(s.data)