from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from goods.models import Goods

User = get_user_model()


class ShoppingCart(models.Model):
    '''
    购物车
    '''
    user = models.ForeignKey(User, verbose_name=u'用户', on_delete=models.DO_NOTHING)
    goods = models.ForeignKey(Goods, verbose_name=u'商品', on_delete=models.DO_NOTHING)
    goods_nums = models.IntegerField(default=0, verbose_name=u'商品数量')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.goods_nums)


class OrderInfo(models.Model):
    '''
    订单
    '''
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("PAYING", "待支付"),
    )
    PAY_TYPE = (
        ('alipay', '支付宝'),
        ('wechat', '微信'),
    )
    user = models.ForeignKey(User, verbose_name=u'用户', on_delete=models.DO_NOTHING)
    order_sn = models.CharField(max_length=30, verbose_name=u'订单号', unique=True)
    trade_no = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"交易号", unique=True)
    pay_status = models.CharField(choices=ORDER_STATUS, max_length=30, default='PAYING', verbose_name=u'订单')
    post_script = models.CharField(max_length=200, verbose_name=u'订单留言')
    order_mount = models.FloatField(default=0.0, verbose_name=u'订单金额')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name=u'支付时间')
    # 用户的一些基本信息

    address = models.CharField(max_length=100, default="", verbose_name="收货地址")
    signer_name = models.CharField(max_length=20, default="", verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11, verbose_name="联系电话")

    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    '''
    订单的详情信息
    '''
    order = models.ForeignKey(OrderInfo, verbose_name=u'订单信息', on_delete=models.DO_NOTHING)
    goods = models.ForeignKey(Goods, verbose_name=u'商品', on_delete=models.DO_NOTHING)
    goods_nums = models.IntegerField(default=0, verbose_name=u'商品数量')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'订单的详情信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
