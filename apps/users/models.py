from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    '''
    用户表
    '''
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name=u'姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name=u'出生年月')
    gender = models.CharField(choices=(('male', u'男'), ('female', '女')), default='female', max_length=11,
                              verbose_name=u'性别')
    mobile = models.CharField(verbose_name=u'电话', max_length=11)
    email = models.EmailField(max_length=100, verbose_name=u'邮箱', null=True, blank=True)

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    '''
    短信验证码
    '''
    code = models.CharField(max_length=10, verbose_name=u'验证码')
    mobile = models.CharField(verbose_name=u'电话', max_length=11)
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
