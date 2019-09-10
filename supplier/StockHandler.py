# -*- coding:utf-8 -*-
import os


class StockHandler:
    def __init__(self):
        self.path = 'd:\\temp\\'

    def getResource(self, productCode):
        try:
            f_idx_name = self.path + productCode + '_idx.txt'
            idx = 0
            if not os.path.isfile(f_idx_name):
                f = open(f_idx_name, 'w')
                f.write( '0' )
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

            # 根据index中记录的行数，找到卡密数据文件中对应的行数+1的数据
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
                print('根据 ' + productCode + " 得到资源：" + con)
                idx += 1
                f = open(f_idx_name, 'w')
                f.write(str(idx))
                f.close()
            return con
        except FileNotFoundError:
            print(productCode + " File is not found.")

        return None
