# -*- coding: utf-8 -*-
from chuangcache.api.RequestUtil import httpPost


class CdnDomainAddRequest(httpPost):
    def __init__(self):
        httpPost.__init__(self)
        self.access_token = None
        self.domain = None
        self.icp_no = None
        self.cdn_type = None
        self.data = None
        self.sourcehost = None
        self.monitor_url = None

    def getapiname(self):
        return '/domain/addDomain'
