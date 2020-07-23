from django.db import models


# Create your models here.


class Product_info(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50, verbose_name='商品名称')
    total_num = models.IntegerField(verbose_name='商品总数')
    product_type = models.CharField(max_length=50, verbose_name='商品类型')
    product_mark = models.CharField(max_length=300, verbose_name='商品简介')
    view_enable = models.CharField(default='y', max_length=1, verbose_name='是否可用')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    common_price = models.DecimalField(max_digits=5,decimal_places=2, verbose_name='商品价格')

    class Meta:
        ordering = ('-id',)
