import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15861754144531'


def get_sign():
    return '3350c61a4bfbe43a2de36a670add6cb5'


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    print(ts)
    return '1586324681588'

form_data={
    'i':'我和你',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'cliend':'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv':'b396e111b686137a6ec711ea651ad37c',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
    }
response=requests.post(url,form_data)
print(response.text)