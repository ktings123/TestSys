from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

HTTP_CHOICE = (
    ('HTTPS', 'https'),
    ('HTTP', 'http'),

)

RE_TYPE = (
    ('GET', 'get'),
    ('POST', 'post'),
    ('PUT', 'put'),
    ('DELETE', 'delete'),

)

parameterType = (
    ('raw', 'raw'),
    ('form-data', 'form-data')
)

projectType = (
    ('Web', 'Web'),
    ('App', 'App')
)


#
# class Usr(AbstractUser):
#     class Meta:
#         ordering = ('-create_time',)


class ProjectList(models.Model):
    id = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=50, verbose_name='名称')
    version = models.IntegerField(verbose_name='版本号')
    projectType = models.CharField(max_length=30, verbose_name='项目类型', choices=projectType)
    desc = models.CharField(max_length=1024, blank=True, null=True, verbose_name='备注')
    status = models.BooleanField(default=False, verbose_name='状态')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.projectName

    def delete(self, using=None, keep_parents=False):
        self.status = True
        self.save()


class ApiInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='接口名称')
    httpType = models.CharField(max_length=50, verbose_name='协议类型', choices=HTTP_CHOICE)
    requestType = models.CharField(max_length=50, verbose_name='请求方式', choices=RE_TYPE)
    header = models.CharField(max_length=1024, verbose_name='请求头')
    apiUrl = models.CharField(max_length=1024, verbose_name='接口地址')
    requestParameterType = models.CharField(max_length=30, verbose_name='参数类型', choices=parameterType)
    requestParameter = models.CharField(max_length=1024, verbose_name='请求参数')
    status = models.BooleanField(default=True, verbose_name='状态')
    productId = models.ForeignKey(ProjectList, on_delete=models.CASCADE, verbose_name='所属项目')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)


class ApiHeaders(models.Model):
    id = models.AutoField(primary_key=True)
    api = models.ForeignKey(ApiInfo, on_delete=models.CASCADE, verbose_name='所属接口')
    head_key = models.CharField(max_length=1024, verbose_name='名称')
    head_value = models.CharField(max_length=1024, verbose_name='值')

    def __str__(self):
        return self.head_key


class ApiParameter(models.Model):
    id = models.AutoField(primary_key=True)
    api = models.ForeignKey(ApiInfo, on_delete=models.CASCADE, verbose_name='所属接口')
    par_key = models.CharField(max_length=1024, verbose_name='名称')
    par_value = models.CharField(max_length=1024, verbose_name='值')
    par_type = models.CharField(default="String", max_length=1024, verbose_name='参数类型',
                                choices=(('Int', 'Int'), ('String', 'String')))
    required = models.BooleanField(default=True, verbose_name="是否必填")
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name="描述")

    def __str__(self):
        return self.par_key


class ApiParRaw(models.Model):
    id = models.AutoField(primary_key=True)
    api = models.ForeignKey(ApiInfo, on_delete=models.CASCADE, verbose_name='所属接口')
    raw_data = models.TextField(blank=True, null=True, verbose_name='内容')


class ApiResponse(models.Model):
    id = models.AutoField(primary_key=True)
    api = models.ForeignKey(ApiInfo, on_delete=models.CASCADE, verbose_name='所属接口')
    res_type = models.CharField(default="String", max_length=1024, verbose_name='参数类型',
                                choices=(('Int', 'Int'), ('String', 'String')))
    res_key = models.CharField(max_length=1024, verbose_name='名称')
    res_value = models.CharField(max_length=1024, verbose_name='值')
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name="描述")


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    taskName = models.CharField(max_length=50, verbose_name='任务名称')
    productId = models.ForeignKey(ProjectList, on_delete=models.CASCADE, verbose_name='所属项目')

    def __str__(self):
        return self.taskName


class TestCase(models.Model):
    id = models.AutoField(primary_key=True)
    caseName = models.CharField(max_length=50, verbose_name='用例名称')
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    project = models.ForeignKey(ProjectList, on_delete=models.CASCADE, verbose_name='所属项目')
    caseId = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='所属任务')

    def __str__(self):
        return self.caseName


class TestResult(models.Model):
    id = models.AutoField(primary_key=True)
    api_id = models.OneToOneField(ApiInfo, on_delete=models.CASCADE, verbose_name='接口')
    res_content = models.CharField(max_length=50, verbose_name='响应内容')
    testResult = models.CharField(max_length=50, verbose_name='测试结果')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
