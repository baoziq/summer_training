# 通用文字识别

# encoding:utf-8

import requests
import base64

'''
通用文字识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
f = open('/Users/baozi/summer_training/day2/demo4.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
# 使用access_token2获取的token
access_token = '24.83da07bf6a8065bfad0925e201de0168.2592000.1722496621.282335-89995986'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())