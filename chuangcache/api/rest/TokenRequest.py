# -*- coding: utf-8 -*-
from chuangcache.api.RequestUtil import httpPost


class TokenRequest(httpPost):
    def __init__(self):
        httpPost.__init__(self)
        self.appid = 'APPID'
        self.appsecret = 'APPSECRETE'
        self.grant_type = 'client_credentials'

    def getapiname(self):
        return '/OAuth/authorize'
