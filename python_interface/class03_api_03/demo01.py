"""
    requests的二次封装
    目的：
        1.同意接口调用的方法，以便于后续的数据驱动实现
        2.让测试用力脚本更干净，整洁
"""
import json

import requests


class HttpClient(object):
    """
    eg: httpclient = HttpClient()
    response = httpclient(method,url,data)
    response = httpclient.send_request(method,utl,data)
    """

    def __init__(self):
        self.session = requests.session()

    def send_request(self, method, url, params_type='form', data=None, **kwargs):
        method = method.upper()
        params_type = params_type.upper()

        # 如果data是字符串，就转换成字典
        if isinstance(data, str):
            data = json.loads(data)

        if "GET" == method:
            response = self.session.request(method=method, url=url, params=data, **kwargs)
        elif "POST" == method:
            if 'FORM' == params_type:  # 发送表单数据，使得data参数传递
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:  # 'json' == params_type:发送json数据，使用json从参数传递
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        else:
            raise ValueError('request method "{}" error'.format(method))
        return response

    def __call__(self, method, url, params_type='form', data=None, **kwargs):
        return self.send_request(method, url, params_type, data, kwargs)

    def close_session(self):
        self.session.close()
