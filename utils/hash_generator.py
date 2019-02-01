# -*- coding: utf-8 -*-

from hashlib import md5


def hash_strings(file):
    start_id = 0
    with open(file) as f:
        list_strings = f.readlines()
    end = len(list_strings) - 1
    while start_id < end:
        hashed = md5((list_strings[start_id]).encode('utf-8')).hexdigest()
        yield hashed
        start_id += 1
