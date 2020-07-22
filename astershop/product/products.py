from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ParseError
from spo.common.apiResponse import ApiResponse
from astershop.serializers import ProductInfoSerializers
from astershop.models import Product_info
from rest_framework.permissions import IsAuthenticated


class Addproduct(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = ProductInfoSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return ApiResponse(msg='success', code=200, data={'id': serializer.data.get('id')})

        else:
            return ApiResponse(msg='fail', code=500, data={'data': serializer.errors})


class ProductView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            produ_obj = Product_info.objects.get(pk=pk)
            serializer = ProductInfoSerializers(produ_obj)
        else:
            queryset = Product_info.objects.all()
            serializer = ProductInfoSerializers(queryset, many=True)
        return ApiResponse(data={'product': serializer.data,
                                 },
                           code=200,
                           msg='success')


class EditProduct(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def push(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = request.data
            produ_obj = Product_info.objects.get(pk=pk)
        except ParseError:
            return ApiResponse(msg='RequestError', code=500, data=ParseError)
        serializer = ProductInfoSerializers(instance=produ_obj, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return ApiResponse(msg='success', code=200, data={'id': serializer.data.get('id')})


class DelProduct(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product_obj = Product_info.objects.get(pk=pk)
        if product_obj.delete():
            return ApiResponse(msg='Del Success', data={'id': pk}, code=200
                         )