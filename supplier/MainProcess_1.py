import sys
import time
import schedule

from lottons.supplier.LogHandler import LogHandler
from lottons.supplier.OrderHandler import OrderHandler
from lottons.supplier.SendSMSHandler import SendSMSHandler
from lottons.supplier.StockHandler import StockHandler


def execute_main_command(startPage):
    logHandler = LogHandler()
    orderHandler = OrderHandler()
    stockHandler = StockHandler()
    sendSMSHandler = SendSMSHandler()

    try:
        saleOrders = orderHandler.queryOrders(startPage)
    except Exception as e:
        print( e )
        sys.exit( 1 )
    if saleOrders is None:
        return False
    for item in saleOrders:
        if item['remarkcolorflag'] is None:
            print( item )
            orderItemId = item['orderItemId']
            remarkcolorflag = item['remarkcolorflag']
            orderId = item['orderId']
            mobilePhone = item['mobilePhone']
            productCode = item['productCode']
            productName = item['productName']
            print( mobilePhone + " " + productCode )
            # resId = stockHandler.getResource( productCode )
            #
            # if resId:
            #     try:
            #         orderHandler.orderDeliver( orderItemId )
            #     except Exception as e:
            #         print( e )
            #         logHandler.logErrorInfo(
            #             "订单" + orderId + "发货失败，已分配库存卡密：" + resId)
            #         sys.exit( 1 )
            #     try:
            #         sendSMSHandler.sendSMS( item, resId )
            #     except Exception as e:
            #         print( e )
            #         logHandler.logErrorInfo(
            #             "订单" + orderId + "发送短信卡密失败,已分配库存卡密：" + resId )
            #         sys.exit( 1 )
            #     print( "订单" + orderId + "已处理， 发送的卡密：" + productCode + " | " + resId )
            #     logHandler.logSuccessInfo( "订单" + orderId + "已处理， 发送的卡密：" + productCode + " | " + resId )
            # else:
            #     print( "订单" + orderId + "未处理，因为 " + productCode + " | " + productName + " 的卡密已用完" )
            #     logHandler.logErrorInfo(
            #         "订单" + orderId + "未处理，因为 " + productCode + " | " + productName + " 的卡密已用完" )
            #     sys.exit( 1 )
    return True


# 被周期性调度触发的函数
def print_time(startTime):
    print("now is", time.strftime('%Y-%m-%d %H:%M:%S'), "enter_the_box_time is" + startTime)
    startPage = 1
    flag = True
    while flag:
        flag = execute_main_command(startPage)
        startPage = startPage + 1


if __name__ == "__main__":
    print('start')
    schedule.every(5).seconds.do(print_time, time.strftime('%Y-%m-%d %H:%M:%S'))
    while True:
        schedule.run_pending()
        time.sleep(1)
