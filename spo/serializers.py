from rest_framework import serializers
from spo.models import parameterType, HTTP_CHOICE, productType, \
    ApiInfo, Usr, ProductList


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

    class Meta:
        model = ProductList
        fields = '__all__'
