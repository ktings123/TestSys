# Generated by Django 3.0.4 on 2020-05-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='接口名称')),
                ('httpType', models.CharField(choices=[('HTTPS', 'HTTP')], max_length=50, verbose_name='协议类型')),
                ('requestType', models.CharField(max_length=50, verbose_name='请求方式')),
                ('baseUrl', models.CharField(max_length=1024, verbose_name='基础地址')),
                ('apiUrl', models.CharField(max_length=1024, verbose_name='接口地址')),
                ('requestParameterType', models.CharField(choices=[('raw', 'raw'), ('form-data', 'form-data')], max_length=30, verbose_name='参数类型')),
                ('requestParameter', models.CharField(max_length=1024, verbose_name='请求参数')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=50, verbose_name='名称')),
                ('version', models.CharField(max_length=30, verbose_name='版本号')),
                ('productType', models.CharField(choices=[('Web', 'Web'), ('App', 'App')], max_length=30, verbose_name='项目类型')),
                ('desc', models.CharField(blank=True, max_length=10000, null=True, verbose_name='备注')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('lastUpdateTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Usr',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50, verbose_name='用戶名称')),
                ('user_id', models.CharField(max_length=50, verbose_name='账号')),
            ],
        ),
    ]
