# -*- coding: utf-8 -*-
from chuangcache.api.RequestUtil import httpPost


class CdnDomainByIdRequest(httpPost):
    def __init__(self):
        httpPost.__init__(self)
        self.access_token = None
        self.domain_id = None

    def getapiname(self):
        return '/domain/getDomainById'
