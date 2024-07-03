# encoding:utf-8

import base64
import requests

'''
图像识别组合API
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
f = open('/Users/baozi/summer_training/day2/demo.jpg', 'rb')
img = base64.b64encode(f.read())
params = {"image":img}
# params = "{\"imgUrl\":\/Users/baozi/summer_training/myenv/day2/demo.jpg,\"scenes\":[\"animal\",\"plant\",\"ingredient\",\"dishs\", \"red_wine\",\"currency\",\"landmark\"]}"
access_token = '24.72c5e2b23aa07e134c733c0d081eeaaa.2592000.1722478097.282335-89934902'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())