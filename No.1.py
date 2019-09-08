# -*- coding: utf-8 -*-
import datetime

import suning.api
import json
# import time


def main():
    # 查询订单的起始和结束时间
    nowTime = datetime.datetime.now()
    startTime = nowTime.strftime("%Y-%m-%d %H:%M:%S")
    endTime = (nowTime - datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
    print("本地时间为 :", startTime)
    print("本地时间为 :", endTime)

    request = suning.api.SaleOrderQueryRequest()
    # localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    request.endTime = startTime
    request.pageNo = "1"
    request.pageSize = "100"
    request.startTime = endTime
    request.state = "10"
    request.supplierCode = "10203337"
    domain = "https://open.suning.com"
    appKey = "ad313b236ba57163e25c4163b1e70c86"
    appSecret = "fc9e9f4ade0511d57c7d99c60f9fdd62"
    request.setDomainInfo(domain, "80")
    request.setAppInfo(appKey, appSecret)
    result = request.getResponse()
    print(result)
    jsonobj = json.loads(result)
    saleOrders = jsonobj['sn_responseContent']['sn_body']['querySaleOrder']
    print(saleOrders)
    for item in saleOrders:
        print(item)


if __name__ == '__main__':
    main()
