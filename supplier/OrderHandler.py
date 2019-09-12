# -*- coding: utf-8 -*-
import datetime

import suning.api
import json


class OrderHandler:
    def __init__(self):
        self.myAppKey = 'aaa'
        self.myAppSecret = 'bb'
        self.requestUrl = 'https://open.suning.com'
        self.domain = 'https://open.suning.com'
        self.supplierCode = '10203337'


    def queryOrders(self):
        request = suning.api.OrdercodeQueryRequest()
        request.startTime = "2019-8-10 00:00:00"
        request.endTime = "2019-8-22 00:00:00"
        request.orderStatus = "20"
        domain = self.requestUrl
        appKey = self.myAppKey
        appSecret = self.myAppSecret

        # 查询订单的起始和结束时间
        nowTime = datetime.datetime.now()
        startTime = nowTime.strftime( "%Y-%m-%d %H:%M:%S" )
        endTime = (nowTime - datetime.timedelta( days=30 )).strftime( "%Y-%m-%d %H:%M:%S" )
        print( "查询开始时间 :", startTime )
        print( "查询结束时间 :", endTime )

        request = suning.api.SaleOrderQueryRequest()
        # localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        request.endTime = startTime
        request.pageNo = "1"    # 起始行
        request.pageSize = "100"    # 每行的记录数，也就是一次处理的量
        request.startTime = endTime
        request.state = "10"    # 查询的订单状态
        request.supplierCode = self.supplierCode
        request.setDomainInfo( domain, "80" )
        request.setAppInfo( appKey, appSecret )
        try:
            jsonobj = request.getResponse
            saleOrders = jsonobj['sn_responseContent']['sn_body']['querySaleOrder']
            return saleOrders
        except Exception as e:
            print(e)

    def orderDeliver(self,orderItemId):
        request = suning.api.OrderDeliverAddRequest()
        # request.expressCompCode = "suning"
        # request.expressNo = "1033439927600"
        request.orderItemId = orderItemId
        # request.sender = "赵钱孙"
        # request.senderTel = "13888888"
        request.sign = "0"
        request.supplierCode = self.supplierCode
        domain = self.domain
        appKey = self.myAppKey
        appSecret = self.myAppSecret
        request.setDomainInfo( domain, "80" )
        request.setAppInfo( appKey, appSecret )
        result = request.getResponse
        print( result )
        return result

if __name__ == "__main__":
    orderHandler = OrderHandler()
    orderHandler.orderDeliver("00426438330103")
