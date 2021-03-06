from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from spo.models import ApiInfo
from spo.serializers import APiSerializers, ApiResponseSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status
import json
import requests
import array


class Api_test_get(APIView):
    """
    即时接口
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        try:
            data = request.data
        except ParseError:
            return Response(status=ParseError.status_code)
        # if isinstance(data, list):
        #     for i in data:
        #         httpType = i['httpType']
        #         data = i['requestParameter']
        #         url = i['apiUrl']
        #         api_url = httpType + url
        #         headers = i['header']
        #         res = requests.post(url=api_url, data=data, headers=headers, timeout=8)
        #         return  Response({
        #             'data_res':ApiResponseSerializers(res).data
        #         })
        # else:
        httpType = data.get('httpType')
        data = data.get('requestParameter')
        url = data.get('apiUrl')
        headers = data.get('header')
        api_url = httpType + "://" + url
        res = requests.post(url=api_url, data=data, headers=headers, timeout=8)
        return Response({
            'data_res': ApiResponseSerializers(res).data
        })
