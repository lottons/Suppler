#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# import httplib
import urllib

from urllib import request
from urllib import parse

# 接口地址
host = "http://api.sms654.com"
# 接口类型 GBK为smsGBK.aspx , UTF-8为smsUTF8.aspx
sms_send_uri = "/smsUTF8.aspx?type=send"

# 用户名
username = "你的用户名"
# 密码，32位MD5大写加密 例:http://tool.chinaz.com/Tools/MD5.aspx
password = "你的密码"
# gwid网关ID号，平台首页可见
gwid = "网关id"


def send_sms(text, mobile):
    data = {"username": username, "password": password, "message": text, "mobile": mobile, "gwid": gwid}
    data = parse.urlencode(data).encode('utf-8')

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    req = urllib.request.Request(host + sms_send_uri, data, headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')

    return html


if __name__ == '__main__':
    mobile = "13913900264"  # 手机号
    text = "【哎呀呀】 你的验证码kicd"  # 内容

    print(send_sms(text, mobile))
