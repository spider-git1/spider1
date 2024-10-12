import requests

headers={
    "Accpet":"application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "}
proxies={
    "http":"http://127.0.0.1:7890",
    "https":"http://127.0.0.1:7890",
}
#请求登录页面

data={
    'usernm':'wys987654321',
    'passwd':'wys123321',
    'authcode':'CJUE',
    'toUrl':'',
    'app':'accountr.aja_login'
}
data={'usernm':"wwwyy",
      'paasswd0':'123456',

      }
r=requests.post('https://www.nowapi.com/?app=account.login', headers=headers,proxies=proxies,data=data)
print(r.text)