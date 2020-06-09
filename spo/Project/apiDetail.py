from spo.models import ApiInfo, Usr
from rest_framework.views import APIView
from spo.serializers import APiSerializers, UsrSerializers
from spo.common.apiResponse import ApiResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ParseError
from rest_framework.response import Response


class ApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def get(self, request):
        queryset = ApiInfo.objects.all().order_by('-id')
        serializer = APiSerializers(queryset, many=True)
        return ApiResponse(data=serializer.data,
                           code=200,
                           msg='success')

    def post(self, request):
        serializer = APiSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return ApiResponse(msg='success', code=200, data={'data': serializer.data.get('id')})
        else:
            return ApiResponse(msg='fail', code=403, data={'data': serializer.errors})


class DetailApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def get_detail(self, pk):
        return ApiInfo.objects.get(pk=pk)

    # 查一个
    def get(self, request, pk):
        try:
            data = request.data
        except ParseError:
            return ApiResponse(msg='RequestError', code=500, data=ParseError)
        serializer = APiSerializers(self.get_detail(pk))
        return ApiResponse(data={'data': serializer.data}, msg='success', code=200)

    # 更新一个
    def post(self, request, pk):
        try:
            data = request.data
        except ParseError:
            return ApiResponse(msg='RequestError', code=500, data=ParseError)
        serializer = APiSerializers(self.get_detail(pk), data=data)
        if self.get_detail(pk) is not None and serializer.is_valid():
            serializer.save()
            return ApiResponse(msg='success', code=200, data={'id': serializer.data.get('id')})

    # 删一个
    def delete(self, request, pk):
        self.get_detail(pk).delete()
        return ApiResponse(msg='success', code=200, data={'data': pk})
