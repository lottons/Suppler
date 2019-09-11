import sys
import time
import schedule

from lottons.supplier.LogHandler import LogHandler
from lottons.supplier.OrderHandler import OrderHandler
from lottons.supplier.SendSMSHandler import SendSMSHandler
from lottons.supplier.StockHandler import StockHandler


def execute_main_command():
    logHandler = LogHandler()
    orderHandler = OrderHandler()
    stockHandler = StockHandler()
    sendSMSHandler = SendSMSHandler()

    try:
        saleOrders = orderHandler.queryOrders()
    except Exception as e:
        print( e )
        sys.exit( 1 )
    for item in saleOrders:
        if item['remarkcolorflag'] is None:
            print( item )
            orderItemId = item['orderItemId']
            remarkcolorflag = item['remarkcolorflag']
            orderId = item['orderId']
            mobilePhone = item['mobilePhone']
            productCode = item['productCode']
            productName = item['productName']
            if remarkcolorflag != '1':
                # print( mobilePhone + " " + productCode )
                resId = stockHandler.getResource( productCode )

                if resId:
                    try:
                        orderHandler.orderDeliver( orderItemId )
                    except Exception as e:
                        print( e )
                        logHandler.logErrorInfo(
                            "订单" + orderId + "发货失败 :" + e)
                        sys.exit( 1 )
                    try:
                        sendSMSHandler.sendSMS( item, resId )
                    except Exception as e:
                        print( e )
                        logHandler.logErrorInfo(
                            "订单" + orderId + "发送短信卡密失败 :" + e )
                        sys.exit( 1 )
                    print( "订单" + orderId + "已处理， 发送的卡密：" + productCode + " | " + resId )
                    logHandler.logSuccessInfo( "订单" + orderId + "已处理， 发送的卡密：" + productCode + " | " + resId )
                else:
                    print( "订单" + orderId + "未处理，因为 " + productCode + " | " + productName + " 的卡密已用完" )
                    logHandler.logErrorInfo(
                        "订单" + orderId + "未处理，因为 " + productCode + " | " + productName + " 的卡密已用完" )
                    sys.exit( 1 )


# 被周期性调度触发的函数
def print_time(startTime):
    print("now is", time.strftime('%Y-%m-%d %H:%M:%S'), "enter_the_box_time is" + startTime)


if __name__ == "__main__":
    print('start')
    schedule.every(5).seconds.do(print_time, time.strftime('%Y-%m-%d %H:%M:%S'))
    time.time()
    while True:
        schedule.run_pending()
        time.sleep(1)
