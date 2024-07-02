# 身份证识别

# encoding:utf-8

import requests
import base64

'''
身份证识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
# 二进制方式打开图片文件
f = open('/Users/baozi/summer_training/day2/demo5.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"id_card_side":"front","image":img}
access_token = '24.72c5e2b23aa07e134c733c0d081eeaaa.2592000.1722478097.282335-89934902'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())