import datetime
import sys
import time
import schedule

from supplier.LogHandler import LogHandler
from supplier.OrderHandler import OrderHandler
from supplier.SendSMSHandler import SendSMSHandler
from supplier.StockHandler import StockHandler


def execute_main_command(startPage, startTime, endTime):
    logHandler = LogHandler()
    orderHandler = OrderHandler()
    stockHandler = StockHandler()
    sendSMSHandler = SendSMSHandler()

    try:
        saleOrders = orderHandler.queryOrders(startPage, startTime, endTime)
        print(saleOrders)
    except Exception as e:
        print(e)
        sys.exit(1)
    if saleOrders is None:
        print("没有查询到订单")
        return False
    else:
        for item in saleOrders:
            remarkcolorflag = item['remarkcolorflag']
            if remarkcolorflag is None:
                orderItemId = item['orderItemId']
                productCode = item['productCode']
                productName = item['productName']
                orderId = item['orderId']

                customerName = item['customerName']
                mobilePhone = item['mobilePhone']

                saleQty = item['saleQty']

                print(customerName + " " + mobilePhone + " " + productCode + " " + productName + " " + saleQty)
                count = 0
                while (count < float(saleQty)):
                    resId = stockHandler.getResource( productCode )
                    print(resId)
                    if resId:
                        try:
                            if count == float(saleQty) - 1:
                                result = orderHandler.orderDeliver( orderItemId )
                                if result != True:
                                    logHandler.logErrorInfo(
                                        "订单" + orderId + "发货失败，调用苏宁发货接口失败。 产品编码：" +  productCode + " | 卡密：" + resId)
                                    break
                                else:
                                    print("订单" + orderId + "发货成功")
                        except Exception as e:
                            print(e)
                            logHandler.logErrorInfo(
                                "订单" + orderId + "发货失败 :" + e)
                            sys.exit(1)

                        try:
                            result = sendSMSHandler.sendSMS(customerName,mobilePhone, productCode, resId )
                            if result != True:
                                logHandler.logErrorInfo(
                                    "订单" + orderId + "发送短信卡密失败，调用短信发送接口失败。产品编码：" +  productCode + " | 卡密：" + resId)
                                break
                            else:
                                print("订单" + orderId + "发货卡密成功")
                        except Exception as e:
                            print( e )
                            logHandler.logErrorInfo(
                                "订单" + orderId + "发送短信卡密失败 :" + e )
                            sys.exit( 1 )

                        print( "订单" + orderId + "已处理， 发送的卡密：" + productCode + " | " + resId )
                        logHandler.logSuccessInfo( "订单" + orderId + "已处理， 发送的卡密：" + mobilePhone + " | " + resId )
                    else:
                        print( "订单" + orderId + "未处理，因为 " + productCode + " | " + productName + " 的卡密已用完" )
                        logHandler.logErrorInfo(
                            "订单" + orderId + "未处理，因为 " + productCode + " | " + productName + " 的卡密已用完" )
                        break

                    count = count + 1
        return True


# 被周期性调度触发的函数
def print_time():
    print("now is", time.strftime('%Y-%m-%d %H:%M:%S'), "开始执行任务：")

    # 查询订单的起始和结束时间
    nowTime = datetime.datetime.now()
    # zeroToday = nowTime - datetime.timedelta(hours=nowTime.hour, minutes=nowTime.minute, seconds=nowTime.second,microseconds=nowTime.microsecond)

    for i in range(4):
        startPage = 1
        # endTime = nowTime.strftime("%Y-%m-%d %H:%M:%S")
        endDay = i * 30
        startDay = (i + 1) * 30
        endTime = (nowTime - datetime.timedelta(days=endDay)).strftime("%Y-%m-%d %H:%M:%S")
        startTime = (nowTime - datetime.timedelta(days=startDay)).strftime("%Y-%m-%d %H:%M:%S")
        flag = True
        print("查询开始时间 :", startTime)
        print("查询结束时间 :", endTime)
        while flag:
            flag = execute_main_command(startPage, startTime, endTime)
            startPage = startPage + 1


if __name__ == "__main__":
    schedule.every(1).minutes.do(print_time)
    while True:
        schedule.run_pending()
        time.sleep(1)
