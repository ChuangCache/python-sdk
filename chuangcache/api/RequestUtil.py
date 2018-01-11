# -*- coding: utf-8 -*-

import json
from urllib import request


class httpPost(object):
    def __init__(self):
        self.__api_base_url = "https://api.chuangcache.com"
        self.__httpmethod = "POST"

    def get_request_header(self):
        return {
            "Content-type": "application/json",
            "Content-Type": "application/json; charset=utf-8",
        }

    def getapiname(self):
        return ""

    def getResponse(self):
        url = self.__api_base_url + self.getapiname()
        data = self.getParameters()
        data = bytes(data, 'utf8')
        req = request.Request(url, headers=self.get_request_header())
        resp = request.urlopen(req, data).read()
        return json.loads(bytes.decode(resp))

    def getParameters(self):
        application_parameter = {}
        for key, value in self.__dict__.items():
            if not key.startswith("__") and not key.startswith("_httpPost__") and value is not None:
                application_parameter[key] = value

        return json.dumps(application_parameter)
