# Generated by Django 3.0.4 on 2020-07-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spo', '0003_auto_20200619_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiinfo',
            name='baseUrl',
        ),
        migrations.AddField(
            model_name='apiinfo',
            name='header',
            field=models.CharField(default='', max_length=1024, verbose_name='请求头'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apiinfo',
            name='response',
            field=models.CharField(default='', max_length=1024, verbose_name='响应内容'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apiinfo',
            name='httpType',
            field=models.CharField(choices=[('HTTPS', 'HTTPS'), ('HTTP', 'HTTP')], max_length=50, verbose_name='协议类型'),
        ),
        migrations.AlterField(
            model_name='apiinfo',
            name='requestType',
            field=models.CharField(choices=[('GET', 'get'), ('POST', 'get'), ('PUT', 'put'), ('DELETE', 'delete')], max_length=50, verbose_name='请求方式'),
        ),
    ]
