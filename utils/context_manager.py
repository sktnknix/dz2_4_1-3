# -*- coding: utf-8 -*-

from datetime import datetime


class TimeScore(object):
    def __enter__(self):
        self.progstart = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Скрипт запустился в ' + str(self.progstart))
        print('Скрипт закончил работу в ' + str(datetime.now()))
        print("Время выполнения: " + str(datetime.now() - self.progstart))
