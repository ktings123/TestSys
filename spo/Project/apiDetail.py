from spo.models import ApiInfo, ProjectList
from rest_framework.views import APIView
from spo.serializers import APiSerializers, ApiHeadersSerializers, \
    ApiParameterSerializers, ApiParRawSerializers
from spo.common.apiResponse import ApiResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated


class ApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            api_obj = ApiInfo.objects.get(pk=pk)
            serializer = APiSerializers(instance=api_obj)
        else:
            queryset = ApiInfo.objects.all().order_by('-id')
            serializer = APiSerializers(queryset, many=True)
        return ApiResponse(data=serializer.data,
                           code=200,
                           msg='success')


class AddApi(ApiView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            data = request.data
        except ParseError:
            return ApiResponse(status=ParseError.status_code, msg='参数错误')
        proj_obj = ProjectList.objects.get(id=data['project_id'])
        serializer = APiSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 先保存接口
            serializer.save(ProjectList=proj_obj)
            # 取出接口ID
            api_id = serializer.data.get('id')
            # 处理接口请求头
            if len(data.get("header")):
                for h in data.get("header"):
                    h['api_id'] = api_id
                    head = ApiHeadersSerializers(data=h)
                    if head.is_valid(raise_exception=True):
                        obj_api = ApiInfo.objects.get(id=api_id)
                        # 保存请求头
                        head.save(ApiInfo=obj_api)
            # 处理接口请求form-data参数
            if data.get('requestParameterType') == 'form-data':
                if len(data.get('requestParameter')):
                    for p in data.get('requestParameter'):
                        p['api_id'] = api_id
                        reqPar = ApiParameterSerializers(data=p)
                        if reqPar.is_valid(raise_exception=True):
                            obj_reqPar = ApiInfo.objects.get(id=api_id)
                            # 保存请求参数
                            reqPar.save(ApiInfo=obj_reqPar)
            # 处理接口请求raw参数
            else:
                if len(data.get('requestParameter')):
                    req_rawPar = ApiParRawSerializers(data=data.get('requestParameter'))
                    if req_rawPar.is_valid(raise_exception=True):
                        obj_rawPar = ApiInfo.objects.get(id=api_id)
                        # 保存请求参数
                        req_rawPar.save(ApiInfo=obj_rawPar)
            return ApiResponse(msg='success', code=200, data={'data': serializer.data.get('id')})
        else:
            return ApiResponse(msg='fail', code=403, data={'data': serializer.errors})


class EditApi(ApiView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

    # 删一个
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        api_obj = ApiInfo.objects.get(pk=pk)
        if api_obj.delete():
            return ApiResponse(msg='success', code=200, data={'data': pk})
