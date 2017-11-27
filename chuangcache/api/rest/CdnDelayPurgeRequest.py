# -*- coding: utf-8 -*-
from chuangcache.api.RequestUtil import httpPost


class CdnDelayPurgeRequest(httpPost):
    def __init__(self):
        httpPost.__init__(self)
        self.access_token = None
        self.is_precache = 0
        self.type = None
        self.urls = None
        self.delay = None

    def getapiname(self):
        return '/content/delayPurge'
