from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from spo.serializers import ProductListSerializers
from spo.common.apiResponse import ApiResponse
from spo.models import ProductList
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated


class AddProduct(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = ProductListSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return ApiResponse(msg='success', code=200, data={'id': serializer.data.get('id')})
        else:
            return ApiResponse(msg='fail', code=500, data={'data': serializer.errors})


class EditProduct(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # 单整体改
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = request.data
            product_obj = ProductList.objects.get(pk=pk)
        except ParseError:
            return ApiResponse(msg='RequestError', code=500, data=ParseError)
        serializer = ProductListSerializers(instance=product_obj, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return ApiResponse(msg='success', code=200, data={'id': serializer.data.get('id')})


class ProductListView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            prod_obj = ProductList.objects.get(pk=pk)
            serializer = ProductListSerializers(prod_obj)

        else:
            queryset = ProductList.objects.all()
            serializer = ProductListSerializers(queryset, many=True)
        return ApiResponse(data={'data': serializer.data,
                                 },
                           code=200,
                           msg='success')


class DelProduct(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product_obj = ProductList.objects.get(pk=pk)
        if product_obj.delete():
            return ApiResponse(msg='Del Success', data={'id': pk}, code=200
                         )
