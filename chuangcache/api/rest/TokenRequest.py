# -*- coding: utf-8 -*-
from chuangcache.api.RequestUtil import httpPost


class TokenRequest(httpPost):
    def __init__(self):
        httpPost.__init__(self)
        self.appid = 'xf3H3si8I0o31ilL'
        self.appsecret = 'Gi3ZbVjCi7Vt1qZxI55JiMuEzQQZCikh'
        self.grant_type = 'client_credentials'

    def getapiname(self):
        return '/OAuth/authorize'
