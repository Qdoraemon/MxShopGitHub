from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Goods

# Create your models here.

User = get_user_model()


class UserFav(models.Model):
    '''
    用户收藏记录表
    '''
    user = models.ForeignKey(User, verbose_name=u'用户',on_delete=models.DO_NOTHING)
    goods = models.ForeignKey(Goods, verbose_name=u'商品', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserLeavingMessage(models.Model):
    '''
    用户留言
    '''
    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购")
    )
    user = models.ForeignKey(User, verbose_name=u'用户',on_delete=models.DO_NOTHING)
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型",
                                       help_text=u"留言类型: 1(留言),2(投诉),3(询问),4(售后),5(求购)")
    subject = models.CharField(max_length=100, default="", verbose_name="主题")
    message = models.TextField(default="", verbose_name="留言内容", help_text="留言内容")
    files = models.FileField(upload_to='message/images/', verbose_name="上传的文件", help_text="上传的文件")
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    '''
    用户收货地址
    '''
    user = models.ForeignKey(User, verbose_name=u'用户',on_delete=models.DO_NOTHING)
    district = models.CharField(max_length=100,default='',verbose_name=u'区域')
    address = models.CharField(max_length=100,default='',verbose_name=u'详细地址')
    signer_name = models.CharField(max_length=100,default='',verbose_name=u'签收人')
    signer_mobile = models.CharField(max_length=11,default='',verbose_name=u'电话')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address

