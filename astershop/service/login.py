from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,

        })


class register(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        usr = data.get('username')
        password = data.get('password')
        email = data.get('email')
        user = User.objects.create_user(username=usr, password=password, email=email)
        if user:
            return Response({
                'user_id':user.pk
            })
