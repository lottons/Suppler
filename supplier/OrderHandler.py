# -*- coding: utf-8 -*-
import datetime

import suning.api
import json


class OrderHandler:
    def __init__(self):
        self.myAppKey = 'ad313b236ba57163e25c4163b1e70c86'
        self.myAppSecret = 'fc9e9f4ade0511d57c7d99c60f9fdd62'
        self.requestUrl = 'https://open.suning.com'
        self.domain = 'https://open.suning.com'
        self.supplierCode = '10203337'

    def queryOrders(self, startPage, startTime, endTime):
        # print(startPage)
        request = suning.api.OrdercodeQueryRequest()
        request.orderStatus = "20"
        domain = self.requestUrl
        appKey = self.myAppKey
        appSecret = self.myAppSecret

        request = suning.api.SaleOrderQueryRequest()
        # localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        request.endTime = endTime
        request.pageNo = startPage  # 起始行
        request.pageSize = "100"  # 每行的记录数，也就是一次处理的量
        request.startTime = startTime
        request.state = "10"  # 查询的订单状态
        request.supplierCode = self.supplierCode
        request.setDomainInfo(domain, "80")
        request.setAppInfo(appKey, appSecret)
        try:
            result = request.getResponse()
            # print(result)
            jsonobj = json.loads(result)
            saleOrders = jsonobj['sn_responseContent']['sn_body']['querySaleOrder']
            #
            # jsonobj = request.getResponse
            # saleOrders = jsonobj['sn_responseContent']['sn_body']['querySaleOrder']
            return saleOrders
        except Exception as e:
            print(e)

    def orderDeliver(self, orderItemId):
        request = suning.api.OrderDeliverAddRequest()
        # request.expressCompCode = "suning"
        # request.expressNo = "1033439927600"
        request.orderItemId = orderItemId
        request.sender = "卞晓斌"
        request.senderTel = "13905170417"
        request.sign = "0"
        request.supplierCode = self.supplierCode
        domain = self.domain
        appKey = self.myAppKey
        appSecret = self.myAppSecret
        request.setDomainInfo(domain, "80")
        request.setAppInfo(appKey, appSecret)
        result = request.getResponse()
        print(result)
        return "result" in result


if __name__ == "__main__":
    orderHandler = OrderHandler()
    result = orderHandler.orderDeliver("00129997883202")
    if result == True:
        print('success')
    else:
        print('fail')
