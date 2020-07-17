from rest_framework import serializers
from astershop.models import Product_info


class ProductInfoSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product_info
        exclude = ['create_time']
