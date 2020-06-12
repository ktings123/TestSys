from rest_framework import serializers
from rest_framework.settings import api_settings
from spo.models import parameterType, HTTP_CHOICE, productType, \
    ApiInfo, Usr, ProductList

dataTimeForm = api_settings.DATE_FORMAT


class APiSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    requestParameterType = serializers.ChoiceField(choices=parameterType)
    httpType = serializers.ChoiceField(choices=HTTP_CHOICE)

    class Meta:
        model = ApiInfo
        fields = '__all__'
        # 查询的时候不包括哪个字段
        # exclude=[]


class UsrSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usr
        fields = '__all__'


class ProductListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    productType = serializers.ChoiceField(choices=productType)

    # lastUpdateTime = serializers.DateTimeField(format=dataTimeForm, input_formats=dataTimeForm, read_only=True)

    class Meta:
        model = ProductList
        # fields = "__all__"
        exclude = ["createTime", "lastUpdateTime"]
