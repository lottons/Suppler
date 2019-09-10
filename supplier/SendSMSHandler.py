# -*- coding:utf-8 -*-


class SendSMSHandler:
    def __init__(self):
        self.path = 'd:\\temp\\tmpl\\'

    def sendSMS(self, orderInfo, resInfo):
        mobilePhone = orderInfo['mobilePhone']
        productCode = orderInfo['productCode']
        # 根据产品code查找模板
        f_tml_name = self.path + productCode + 'tml.txt'
        f_tml = open( f_tml_name )
        aLine = f_tml.readline()
        f_tml.close()
        contxt = aLine.format(mobilePhone, resInfo)
        print(contxt)
        # 调用api发送短信

