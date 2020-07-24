from spo.models import ApiInfo
from rest_framework.views import APIView
from spo.serializers import APiSerializers
from spo.common.apiResponse import ApiResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ParseError


class ApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            api_obj = ApiInfo.objects.get(pk=pk)
            serializer = APiSerializers(instance=api_obj)
        else:
            queryset = ApiInfo.objects.all().order_by('-id')
            serializer = APiSerializers(queryset, many=True)
        return ApiResponse(data={serializer.data},
                           code=200,
                           msg='success')


class AddApi(ApiView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def post(self, request):
        serializer = APiSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return ApiResponse(msg='success', code=200, data={'data': serializer.data.get('id')})
        else:
            return ApiResponse(msg='fail', code=403, data={'data': serializer.errors})


class EditApi(ApiView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk")
            data = request.data
            api_obj = ApiInfo.objects.get(pk=pk)
        except ParseError:
            return ApiResponse(msg='RequestError', code=500, data=ParseError)
        serializer = APiSerializers(instance=api_obj, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return ApiResponse(msg='success', code=200, data={'id': serializer.data.get('id')})


class DetailApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    # 查一个
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            api_obj = ApiInfo.objects.get(pk=pk)
        except ParseError:
            return ApiResponse(msg='RequestError', code=500, data=ParseError)
        serializer = APiSerializers(instance=api_obj)
        return ApiResponse(data={'id': serializer.data.get('id')}, msg='success', code=200)


class DelApi(ApiView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    # 删一个
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        api_obj = ApiInfo.objects.get(pk=pk)
        if api_obj.delete():
            return ApiResponse(msg='success', code=200, data={'data': pk})
