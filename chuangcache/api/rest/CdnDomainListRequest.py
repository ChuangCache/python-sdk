# -*- coding: utf-8 -*-
from chuangcache.api.RequestUtil import httpPost


class CdnDomainListRequest(httpPost):
    def __init__(self):
        httpPost.__init__(self)
        self.access_token = None

    def getapiname(self):
        return '/domain/domainList'
