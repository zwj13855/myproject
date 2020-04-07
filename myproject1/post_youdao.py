import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'i':'我和你',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'cliend':'fanyideskweb',
    'salt':'15861754144531',
    'sign':'3350c61a4bfbe43a2de36a670add6cb5',
    'ts':'1586175414453',
    'bv':'b396e111b686137a6ec711ea651ad37c',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
    }
response=requests.post(url,form_data)
print(response.text)