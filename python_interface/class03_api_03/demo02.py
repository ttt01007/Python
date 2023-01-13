'''
封装签名
'''
import configparser
import os
from hashlib import md5
import time
from Python.python_interface.class03_api_03.demo01 import HttpClient


class ShowAPI(object):
    '''发送showapi平台的接口'''
    API_URL = "https://route.showapi.com"

    def __init__(self, showapi_appid=None, secret_key=None):
        config = configparser.ConfigParser
        config_dir = '\env.ini'
        config.read(config_dir, encoding='utf-8')
        if showapi_appid is None:
            self.showapi_appid = config.get('showapi', 'SHOWAPI_APPID')
        if secret_key is None:
            self.secret_key = config.get('showapi', 'SECRET_ID')

        self.showapi_appid = showapi_appid
        self.secret_key = secret_key

    def gen_signature(self, params=None):
        buff = ''
        for k in sorted(params.keys()):
            buff += str(k) + str(params[k])
            return md5(buff.encode("utf-8")).hexdigest()

    def send(self, path, method, params):
        params['showapi_appid'] = self.showapi_appid
        params['showapi_sing'] = self.gen_signature()

        try:
            httpclient = HttpClient()
            url = self.API_URL + '/' + path
            r = httpclient.send_request(method=method, url=url, params_type='form', data=params)
            httpclient.close_session()
            return r
        except Exception as ex:
            print('调用接口失败', str(ex))
