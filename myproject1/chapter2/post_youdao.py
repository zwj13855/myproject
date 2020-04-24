import random
import requests
import time
import json
import hashlib
class Youdao():
    def __init__(self,content):
        self.content=content
        self.url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt
        self.sign=self.get_sign()


    def get_salt(self):

        #print("random = ",s)
        #print("ts = ",t)
        #print("salt =",t+s)
        return  self.ts+str(random.randint(0,10))
        #return '15861754144531'

    def get_md5(self,value):

        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        i=self.ts
        e=self.content
        s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        #print("s=",s ,"md5=",get_md5(s))
        return self.get_md5(s)
        #return '3350c61a4bfbe43a2de36a670add6cb5'


    def get_ts(self):
        t = time.time()
       #print("ts=", str(int(round(t * 1000))))
        return str(int(round(t * 1000)))
        #return '1586324681588'



   #def get_content(self):
    #   return self.content

    def yield_form_data(self):
        form_data={
            'i': self.content,
            'from':'AUTO',
            'to':'AUTO',
            'smartresult':'dict',
            'cliend':'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv':'b396e111b686137a6ec711ea651ad37c',
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_REALTlME',
        }
        return form_data

    def get_headers(self):
        headers={
            'Cookie':'OUTFOX_SEARCH_USER_ID=-1665335869@10.108.160.17; OUTFOX_SEARCH_USER_ID_NCOO=1037945139.8982772; _ntes_nnid=a97800a79faac1bc034b1dc63009ef6d,1586156942958; JSESSIONID=aaaxFY9j18aDR93vcfYfx; ___rl__test__cookies=1586756909233',
            'Referer':'http://fanyi.youdao.com/',
            'User-Agent':'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 75.0.3770.100 Safari / 537.36',
        }
        return headers
    def fanyi(self):
        response =requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        content=json.loads(response.text)
        return content['translateResult'][0][0]['tgt']

if __name__ == '__main__':
  # print(get_headers())
  # response=requests.post(url, data=form_data,haeders=get_headers())
    while(True):
        try:
            i= input("please input : ")
            youdao= Youdao(i)
            print("fanyi result :",youdao.fanyi())
        except:
            pass







