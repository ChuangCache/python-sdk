# -*- coding: utf-8 -*-
from chuangcache.api.RequestUtil import httpPost


class CdnGetDelayPurgeListRequest(httpPost):
    def __init__(self):
        httpPost.__init__(self)
        self.access_token = None
        self.task_id = None
        self.url_name = None
        self.start_time = None
        self.end_time = None
        self.page = 0
        self.page_num = 50

    def getapiname(self):
        return '/content/getDelayPurgeList'
