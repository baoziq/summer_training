# 图像单主体识别
# encoding:utf-8

import requests
import base64

'''
图像主体检测
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"
# 二进制方式打开图片文件
f = open('/Users/baozi/summer_training/day2/demo2.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img,"with_face":1}
# 使用access_token1获取的token
access_token = '24.72c5e2b23aa07e134c733c0d081eeaaa.2592000.1722478097.282335-89934902'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())