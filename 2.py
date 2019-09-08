# -*- coding:utf-8 -*-
# SquareSpiral1.py - Draws a square spiral

import datetime
import os
import time
import json
import turtle

ticks = time.time()
print("当前时间戳为:", ticks)

nowTime = datetime.datetime.now()
startTime = nowTime.strftime("%Y-%m-%d %H:%M:%S")
endTime = (nowTime - datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
print("本地时间为 :", startTime)
print("本地时间为 :", endTime)

msg = '{"sn_responseContent":{"sn_head":{"pageTotal":1,"pageNo":1,"totalSize":15,"returnMessage":"biz.handler.data-get:success"},"sn_body":{"querySaleOrder":[{"memberOrgName":"","remarkcolorflag":"1","supplierremark":"客户退货","orderItemId":"00118954071301","posId":"AJ37075439","orderId":"38110234522","status":"10","productName":"CIBN 超级会员高清影视VIP 月卡","productCode":"11168530833","supplierCode":"10203337","telephone":null,"mobilePhone":"13103919307","shipCondition":"01","customerName":"宋小涛","address":"河南省焦作市沁阳市西万镇河南省焦作市沁阳西万镇西万村德隆超市附近","remark":null,"saleTime":"2019-09-06 17:17:35","price":"30.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":"1","supplierremark":"客户退货","orderItemId":"00118887834801","posId":"AJ36795532","orderId":"37109979778","status":"10","productName":"腾讯（Tencent）腾讯视频VIP会员1个月腾讯好莱坞视频一个月vip会员月卡","productCode":"11095843044","supplierCode":"10203337","telephone":null,"mobilePhone":"13928770931","shipCondition":"01","customerName":"李先生","address":"江西省南昌市青山湖区全区北京东路东方银座三楼苏宁易购办公区","remark":null,"saleTime":"2019-09-06 01:21:47","price":"19.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":"1","supplierremark":"客户退货","orderItemId":"00118397570202","posId":"AJ34101100","orderId":"39109775371","status":"10","productName":"腾讯（Tencent）腾讯视频VIP会员1个月腾讯好莱坞视频一个月vip会员月卡","productCode":"11095843044","supplierCode":"10203337","telephone":null,"mobilePhone":"13311638350","shipCondition":"01","customerName":"陈春燕","address":"上海上海市嘉定区全区马陆镇德富路900弄8号1101室","remark":null,"saleTime":"2019-08-31 11:36:40","price":"21.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":null,"supplierremark":null,"orderItemId":"00424520515702","posId":"MA12660877","orderId":"34422730517","status":"10","productName":"CIBN 超级会员高清影视VIP 月卡","productCode":"11168530833","supplierCode":"10203337","telephone":null,"mobilePhone":"13485695277","shipCondition":"01","customerName":"江华","address":"安徽省合肥市包河区全区京华世家21幢1001室","remark":null,"saleTime":"2019-08-27 07:01:36","price":"30.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":"1","supplierremark":"客户退货","orderItemId":"00424499065301","posId":"MA12579693","orderId":"36422682288","status":"10","productName":"腾讯（Tencent）腾讯视频VIP会员1个月腾讯好莱坞视频一个月vip会员月卡","productCode":"11095843044","supplierCode":"10203337","telephone":null,"mobilePhone":"13702061235","shipCondition":"01","customerName":"郭磊","address":"天津市天津市武清区全区前进道1066号创意米兰招商中心","remark":null,"saleTime":"2019-08-24 12:51:29","price":"21.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":null,"supplierremark":null,"orderItemId":"00135366756002","posId":"AM66441048","orderId":"36129809807","status":"10","productName":"CIBN 超级会员高清影视VIP 月卡","productCode":"11168530833","supplierCode":"10203337","telephone":null,"mobilePhone":"18036929911","shipCondition":"01","customerName":"宋先生","address":"江苏省宿迁市宿城区全区金水名都-5幢","remark":null,"saleTime":"2019-08-20 13:48:21","price":"30.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":"1","supplierremark":"客户退货","orderItemId":"00135185829502","posId":"AM65226375","orderId":"40129825006","status":"10","productName":"CIBN 超级会员高清影视VIP 月卡","productCode":"11168530833","supplierCode":"10203337","telephone":null,"mobilePhone":"13927759089","shipCondition":"01","customerName":"何金华","address":"广东省佛山市禅城区祖庙街道东方广场电联","remark":null,"saleTime":"2019-08-19 15:15:36","price":"30.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":"1","supplierremark":"客户退货","orderItemId":"00135043495403","posId":"AM64034308","orderId":"33129649281","status":"10","productName":"CIBN 超级会员高清影视VIP 月卡","productCode":"11168530833","supplierCode":"10203337","telephone":null,"mobilePhone":"18715315935","shipCondition":"01","customerName":"周桃芜","address":"安徽省芜湖市弋江区全区利民路江城国际瑞虹苑2-1-1001","remark":null,"saleTime":"2019-08-18 22:55:45","price":"30.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":"1","supplierremark":"客户退货","orderItemId":"00134207560702","posId":"AM55969123","orderId":"33129122767","status":"10","productName":"CIBN 超级会员高清影视VIP 月卡","productCode":"11168530833","supplierCode":"10203337","telephone":null,"mobilePhone":"13914598660","shipCondition":"01","customerName":"丹丹","address":"江苏省镇江市句容市句容市句容市二圣镇自然村","remark":null,"saleTime":"2019-08-18 13:37:54","price":"30.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":null,"supplierremark":null,"orderItemId":"00134769064202","posId":"AM61123222","orderId":"35129546909","status":"10","productName":"CIBN 超级会员高清影视VIP 月卡","productCode":"11168530833","supplierCode":"10203337","telephone":null,"mobilePhone":"13427216628","shipCondition":"01","customerName":"梁雪屏","address":"广东省江门市新会区双水镇小冈天台南水管理区长康村097号","remark":null,"saleTime":"2019-08-18 13:12:13","price":"30.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":"1","supplierremark":"客户退货","orderItemId":"00134601792103","posId":"AM59555491","orderId":"39129495011","status":"10","productName":"CIBN 超级会员高清影视VIP 月卡","productCode":"11168530833","supplierCode":"10203337","telephone":null,"mobilePhone":"18251999745","shipCondition":"01","customerName":"胡传志","address":"江苏省南京市六合区全区瓜埠镇 贾裴村 贾裴村胡庄路","remark":null,"saleTime":"2019-08-18 06:37:55","price":"30.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":null,"supplierremark":null,"orderItemId":"00134543205203","posId":"AM58798690","orderId":"36129347403","status":"10","productName":"CIBN 超级会员高清影视VIP 月卡","productCode":"11168530833","supplierCode":"10203337","telephone":null,"mobilePhone":"18561250820","shipCondition":"01","customerName":"曲尧基","address":"辽宁省大连市甘井子区全区泡崖子八区玉丽街37号1-502","remark":null,"saleTime":"2019-08-18 00:08:11","price":"30.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":"1","supplierremark":"客户退货","orderItemId":"00133548421802","posId":"AM51302855","orderId":"32128913753","status":"10","productName":"CIBN 超级会员高清影视VIP 月卡","productCode":"11168530833","supplierCode":"10203337","telephone":null,"mobilePhone":"15858143680","shipCondition":"01","customerName":"黄剑","address":"湖北省黄冈市黄梅县黄梅镇龙凤花园7幢二单元303","remark":null,"saleTime":"2019-08-14 08:09:33","price":"30.000","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":"1","supplierremark":"客户退货","orderItemId":"00132727148301","posId":"AM46311983","orderId":"33128477834","status":"10","productName":"腾讯（Tencent）腾讯视频vip会员3个月腾讯vip好莱坞视屏会员季卡三个月","productCode":"11095843048","supplierCode":"10203337","telephone":null,"mobilePhone":"13813997537","shipCondition":"01","customerName":"华俊杰","address":"江苏省南京市雨花台区全区华为南京研究所软件大道101号","remark":null,"saleTime":"2019-08-09 21:33:56","price":"58.010","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"},{"memberOrgName":"","remarkcolorflag":"1","supplierremark":"客户退货","orderItemId":"00132590166701","posId":"AM45736827","orderId":"31128439652","status":"10","productName":"腾讯（Tencent）腾讯视频VIP会员1个月腾讯好莱坞视频一个月vip会员月卡","productCode":"11095843044","supplierCode":"10203337","telephone":null,"mobilePhone":"17636403157","shipCondition":"01","customerName":"赵世雄","address":"山西省长治市武乡县丰州镇国税局对面宏伟干洗店","remark":null,"saleTime":"2019-08-09 13:58:43","price":"20.010","platform":"A","saleQty":"1.000","returnFlag":"0","returnorderflag":"0","returnStatus":null,"supplierCmmdtyCode":"10203337","orderItemBizType":"8","wareCode":"","exchangeGoodsFlag":"0"}]}}}'
jsonobj = json.loads(msg)

saleOrders = jsonobj['sn_responseContent']['sn_body']['querySaleOrder']
print(saleOrders)
for item in saleOrders:
    print(item)
    orderItemId = item['orderItemId']
    remarkcolorflag = item['remarkcolorflag']
    orderId = item['orderId']
    mobilePhone = item['mobilePhone']
    productCode = item['productCode']
    if remarkcolorflag != '1':
        print(mobilePhone + " " + productCode)
        try:
            f_idx_name = 'd:/temp/' + productCode + '_idx.txt'
            idx = 0
            if not os.path.isfile(f_idx_name):
                f = open(f_idx_name, 'w')
                f.write('0')
                f.close()
            else:
                f_idx = open(f_idx_name)
                idx = int(f_idx.readline())
                f_idx.close()
            # print(idx)

            f_con_name = 'd:\\temp\\' + productCode + '.txt'
            # print(f_con_name)
            f_con = open(f_con_name)

            t_idx = 0
            con = ''

            while True:
                if t_idx > idx:
                    break

                aLine = f_con.readline()
                t_idx += 1
                con = aLine

            f_con.close()

            if con == '':
                print(productCode + ' 卡密已用完')
            else:
                print('待发送卡密 ' + con)
                idx += 1
                f = open(f_idx_name, 'w')
                f.write(str(idx))
                f.close()
        except FileNotFoundError:
            print(productCode + " File is not found.")

# t = turtle.Pen()
# # for x in range(100):
# #     t.forward(x)
# #     t.left(90)
