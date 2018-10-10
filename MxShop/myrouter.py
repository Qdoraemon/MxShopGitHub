# -*- coding: utf-8 -*-
__author__ = 'smalldoraemon'
__date__ = '2018/6/21 14:13'

import socket
import random
# from django_MoOnline_school import settings
# 获取setting配置
from django.conf import settings

'''
    测试连接(为了安全连接一下)
    @:param database_name 从数据库的名字
'''


def test_connection_to_db(database_name):
    try:
        db_definition = getattr(settings, 'DATABASES')[database_name]
        s = socket.create_connection((db_definition['HOST'], 3306), 2)
        s.close()
        return True
    except (AttributeError, socket.timeout) as e:
        return False


'''
    读写分离操作    
'''


class Router(object):
    # 读操作
    def db_for_read(self, model, **hints):
        # 随机获取从数据库名字
        slave_name = random.choice(settings.DATABASE_KEYS_LIST)
        if test_connection_to_db(slave_name) and settings.READ_AND_WRITE_SEPARATION:
            return slave_name

        return 'default'

    # 写操作
    def db_for_write(self, model, **hints):
        "Point all writes to the default db"
        return 'default'

    ''' 
    这个一定要 不然关联数据库操作会错误 True 是可以 。 None 是默认
    '''
    def allow_relation(self, obj1, obj2, **hints):
        """是否运行关联操作"""
        return True
