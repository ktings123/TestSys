from rest_framework import serializers
from rest_framework.settings import api_settings
from spo.models import parameterType, HTTP_CHOICE, projectType, \
    ApiInfo, ProjectList, Task, TestCase

dataTimeForm = api_settings.DATE_FORMAT


class APiSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    requestParameterType = serializers.ChoiceField(choices=parameterType)
    httpType = serializers.ChoiceField(choices=HTTP_CHOICE)
    productId = serializers.IntegerField(read_only=True)

    class Meta:
        model = ApiInfo
        fields = '__all__'
        # 查询的时候不包括哪个字段
        # exclude=[]


#
# class UsrSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Usr
#         fields = '__all__'


class ProductListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    productType = serializers.ChoiceField(choices=projectType)

    # lastUpdateTime = serializers.DateTimeField(format=dataTimeForm, input_formats=dataTimeForm, write_only=True)

    class Meta:
        model = ProjectList
        # fields = "__all__"
        exclude = ["createTime", "lastUpdateTime"]


class TaskSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


class TestCaseSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TestCase
        fields = "__all__"
