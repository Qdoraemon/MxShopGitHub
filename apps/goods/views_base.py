# -*- coding: utf-8 -*-

# Author: smalldoraemon@qq.com
# CreateTime: 2018/10/9 10:51 PM

from django.views.generic.base import View
from goods.models import Goods
from django.http import HttpResponse
import json
class GoodsListView(View):
    def get(self,request):
        '''
        通过django的view实现商品列表页
        :param request:
        :return:
        '''
        json_list = []
        goods_list = Goods.objects.all()[:10]
        for good in goods_list:
            json_dict = {}
            json_dict['name'] = good.name
            json_dict['category'] = good.category.name
            json_dict['market_price'] = good.market_price
            json_list.append(json_dict)

        return HttpResponse(json.dumps(json_list), content_type='application/json')