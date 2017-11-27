# -*- coding: utf-8 -*-
from chuangcache.api.RequestUtil import httpPost


class CdnPurgeRequest(httpPost):
    def __init__(self):
        httpPost.__init__(self)
        self.access_token = None
        self.api_type = 0
        self.type = None
        self.urls = None

    def getapiname(self):
        return '/content/purge'
