# -*- coding: utf-8 -*-
import chuangcache.api

tokenRequest = chuangcache.api.rest.TokenRequest()
resp = tokenRequest.getResponse()
print(resp['data']['access_token'])

cdnDomainListRequest = chuangcache.api.rest.CdnDomainListRequest()
cdnDomainListRequest.access_token = resp['data']['access_token']
resp = cdnDomainListRequest.getResponse()
print(resp)