# -*- coding: utf-8 -*-
from chuangcache.api.RequestUtil import httpPost


class CdnStatisticsRequest(httpPost):
    def __init__(self):
        httpPost.__init__(self)
        self.access_token = None
        self.domain = None
        self.starttime = None
        self.endtime = None
        self.type = None
        self.resulttype = 0

    def getapiname(self):
        return '/history/getdata'
