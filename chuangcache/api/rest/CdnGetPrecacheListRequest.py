# -*- coding: utf-8 -*-
from chuangcache.api.RequestUtil import httpPost


class CdnGetPrecacheListRequest(httpPost):
    def __init__(self):
        httpPost.__init__(self)
        self.access_token = None
        self.start_time = None
        self.page = 0
        self.page_num = 50

    def getapiname(self):
        return '/content/getPreCacheList'
