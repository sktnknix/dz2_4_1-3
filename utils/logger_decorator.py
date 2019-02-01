# -*- coding: utf-8 -*-

import datetime


def path_to_logging(path):
    def logger(func):
        def new_func(*args, **kwargs):
            start_time = datetime.datetime.now()
            res = func(*args, **kwargs)
            result = '\n****************************\nФункция: ' + func.__name__ + ' стартовала: ' + \
                     str(start_time) + ' завершилась: ' + str(datetime.datetime.now()) + '\n время работы: ' + \
                     str(datetime.datetime.now() - start_time) + '\n аргументы: ' + str(args) + \
                     str(kwargs)
            with open(path, 'a') as file:
                file.write(result)
            return res
        return new_func
    return logger
