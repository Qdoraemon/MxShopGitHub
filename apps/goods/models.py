from django.db import models

from DjangoUeditor.models import UEditorField


# Create your models here.

class GoodsCategory(models.Model):
    '''
    商品类别
    '''
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )
    name = models.CharField(default='', max_length=30, verbose_name=u'类别名', help_text=u'类别名')
    code = models.CharField(default='', max_length=30, verbose_name=u'类别code', help_text=u'类别code')
    desc = models.TextField(default='', verbose_name=u'类别描述', help_text=u'类别描述')
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name=u'类目级别', help_text=u'类目级别')
    parent_category = models.ForeignKey('self', null=True, blank=True, verbose_name=u'父类别', help_text=u'父类别',
                                        related_name=u'sub_cat',on_delete=models.DO_NOTHING)  # self 外键指向自己 做无限分类用的
    is_tab = models.BooleanField(default=False, verbose_name=u'是否导航', help_text=u'是否导航')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    '''
    品牌的名称
    '''
    category = models.ForeignKey(GoodsCategory,null=True,blank=True,verbose_name=u'商品类别的名称',on_delete=models.DO_NOTHING)
    name = models.CharField(default='', max_length=30, verbose_name=u'品牌名', help_text=u'品牌名')
    desc = models.TextField(default='', max_length=200, verbose_name=u'品牌描述', help_text=u'品牌描述')
    image = models.ImageField(upload_to='brands/', max_length=200)
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'品牌的名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    '''
    商品详情
    '''
    category = models.ForeignKey(GoodsCategory, null=True, blank=True, verbose_name=u'商品类目',on_delete=models.DO_NOTHING)
    goods_sn = models.CharField(max_length=50, default='', verbose_name=u'商品唯一货号')
    name = models.CharField(max_length=300, verbose_name=u'商品名')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    sold_num = models.IntegerField(default=0, verbose_name=u'商品销售量')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏数')
    goods_num = models.IntegerField(default=0, verbose_name=u'库存数')
    market_price = models.FloatField(default=0, verbose_name=u'市场价格')
    shop_price = models.FloatField(default=0, verbose_name=u'本店价格')
    goods_brief = models.TextField(max_length=500, verbose_name=u'商品简短描述')
    goods_desc = UEditorField(verbose_name=u'内容', imagePath='goods/images', width=950, height=300,
                              filePath='goods/files', default='')
    ship_free = models.BooleanField(default=True, verbose_name=u'是否承担运费')
    goods_font_image = models.ImageField(upload_to='goods/images/', null=True, blank=True, verbose_name=u'封面图')
    is_new = models.BooleanField(default=False, verbose_name=u'是否新品')
    is_hot = models.BooleanField(default=False, verbose_name=u'是否热销')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'商品详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    '''
    商品图片
    '''
    goods = models.ForeignKey(Goods, verbose_name=u'商品', related_name='images',on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='goods/images', verbose_name=u'图片', null=True, blank=True)
    # image_url = models.CharField(max_length=255,null=True,blank=True,verbose_name=u'图片url')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    '''
    轮播图
    '''
    goods = models.ForeignKey(Goods, verbose_name=u'商品',on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='banner', verbose_name=u'轮播图片')
    index = models.IntegerField(default=0, verbose_name=u'轮播顺序')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播商品图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
