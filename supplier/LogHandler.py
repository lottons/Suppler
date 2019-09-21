import datetime
import os


class LogHandler:
    def __init__(self):
        self.path = 'd:\\temp\\log\\'

    def logSuccessInfo(self, msg):
        try:
            f_success = self.path + '_success.txt'
            if not os.path.isfile(f_success):
                f = open(f_success, 'a')
                f.write(msg + '')
                f.close()
            else:
                f = open(f_success, 'a')
                f.write(msg + '')
                f.close()
        except FileNotFoundError:
            print(" File is not found.")

    def logErrorInfo(self, msg):
        try:
            f_error = self.path + '_error.txt'
            if not os.path.isfile(f_error):
                f = open(f_error, 'a')
                f.write(msg + '\n')
                f.close()
            else:
                f = open(f_error, 'a')
                f.write(msg + '\n')
                f.close()
        except FileNotFoundError:
            print(" File is not found.")
