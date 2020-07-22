from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.conf import settings
from rest_framework import status

import datetime
from rest_framework.authentication import TokenAuthentication

EXPIRE_MINUTES = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES', 1)


# 登录&签发token
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            time = datetime.datetime.now()
            if created or token.created < time - datetime.timedelta(minutes=EXPIRE_MINUTES):
                token.delete()
                token = Token.objects.create(user=serializer.validated_data['user'])
                token.created = time
                token.save()
            return Response({
                'token': token.key,
                'user_id': user.pk,

            })
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


obtain_auth_token = CustomAuthToken.as_view()


# 注册
class register(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        usr = data.get('username')
        password = data.get('password')
        email = data.get('email')
        user = User.objects.create_user(username=usr, password=password, email=email)
        if user:
            return Response({
                'user_id': user.pk
            })


# 登出
class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response({
            'message': 'logout success'
        })


# 改密码
class ChangePwd(APIView):
    def post(self, request):
        username = request.data.get('username')
        old_password = request.data.get('oldPassword')
        new_password = request.data.get('NewPassword')
        u = User.objects.get(username=username)
        p = u.check_password(old_password)
        if u and p:
            u.set_password(new_password)
            u.save()
            return Response({
                'message': 'ChangePassword Success',
                'user_id': u.pk
            })
        else:
            return Response({
                'message': '账号/密码错误'
            })
