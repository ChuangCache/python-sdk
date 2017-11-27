# -*- coding: utf-8 -*-
from chuangcache.api.RequestUtil import httpPost


class CdnLogRequest(httpPost):
    def __init__(self):
        httpPost.__init__(self)
        self.access_token = None
        self.domain = None
        self.starttime = None
        self.endtime = None

    def getapiname(self):
        return '/cdnlog/logfiles'
