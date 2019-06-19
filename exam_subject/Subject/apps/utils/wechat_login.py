# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/4/25 0025 13:28'

import requests
import json
from Subject import settings


class WxLogin(object):
    '''微信登录'''
    def __init__(self):
        self.grant_type = "authorization_code"
        self.appid = settings.APP_ID
        self.secret = settings.APP_KEY

    def getUserInfo(self, js_code):
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}&js_code={JSCODE}&grant_type=authorization_code'. \
            format(APPID=self.appid, SECRET=self.secret, JSCODE=js_code)
        userInfo = requests.get(url=url)
        userInfo_dict = json.loads(userInfo.text)
        userInfo_dict.pop('session_key', None)
        print(userInfo_dict)
        return userInfo_dict


def mian():
    wx = WxLogin()
    wx.getUserInfo('033x0kK31bktQQ171MJ310IiK31x0kKI')


if __name__ == '__main__':
    mian()