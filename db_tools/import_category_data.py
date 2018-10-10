# -*- coding: utf-8 -*-

# Author: smalldoraemon@qq.com
# CreateTime: 2018/10/9 6:56 AM

# 以下说明了django的model单独使用
import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + '../')  # 设置路径
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")  # 设置环境变量

# 有以下这两个就可以直接使用django
import django

django.setup()

from goods.models import GoodsCategory

# 添加数据
from db_tools.data.category_data import row_data


def add_data(data, type, parent_instance=None):
    '''
    填充数据用的
    :param data: 数据主体
    :param type: 类型
    :param parent_instance: 父类实体
    :return goods 实例主体:
    '''
    goods = GoodsCategory()

    goods.code = data['code']
    goods.name = data['name']
    goods.category_type = type
    if parent_instance is not None:
        goods.parent_category = parent_instance
    goods.save()
    return goods


if __name__ == '__main__':
    for level_cat_one in row_data:
        level_instance_one = add_data(level_cat_one, 1)
        for level_cat_two in level_cat_one['sub_categorys']:
            level_instance_two = add_data(level_cat_two, 2,level_instance_one)
            for level_cat_there in level_cat_two['sub_categorys']:
                level_instance_there = add_data(level_cat_there, 3, level_instance_two)
