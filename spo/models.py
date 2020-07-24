from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

HTTP_CHOICE = (
    ('HTTPS', 'HTTPS'),
    ('HTTP', 'HTTP'),

)

RE_TYPE = (
    ('GET', 'get'),
    ('POST', 'get'),
    ('PUT', 'put'),
    ('DELETE', 'delete'),

)

parameterType = (
    ('raw', 'raw'),
    ('form-data', 'form-data')
)

productType = (
    ('Web', 'Web'),
    ('App', 'App')
)

#
# class Usr(AbstractUser):
#     class Meta:
#         ordering = ('-create_time',)


class ProductList(models.Model):
    id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=50, verbose_name='名称')
    version = models.IntegerField(verbose_name='版本号')
    productType = models.CharField(max_length=30, verbose_name='项目类型', choices=productType)
    desc = models.CharField(max_length=10000, blank=True, null=True, verbose_name='备注')
    # status = models.BooleanField(default=True,verbose_name='状态')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    lastUpdateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')


class ApiInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='接口名称')
    httpType = models.CharField(max_length=50, verbose_name='协议类型', choices=HTTP_CHOICE)
    requestType = models.CharField(max_length=50, verbose_name='请求方式', choices=RE_TYPE)
    header = models.CharField(max_length=1024, verbose_name='请求头')
    apiUrl = models.CharField(max_length=1024, verbose_name='接口地址')
    requestParameterType = models.CharField(max_length=30, verbose_name='参数类型', choices=parameterType)
    requestParameter = models.CharField(max_length=1024, verbose_name='请求参数')
    response = models.CharField(max_length=1024, verbose_name='响应内容')
    status = models.BooleanField(default=True, verbose_name='状态')
    productId = models.ForeignKey(ProductList, on_delete=models.CASCADE, verbose_name='所属项目')

    class Meta:
        ordering = ('-id',)
