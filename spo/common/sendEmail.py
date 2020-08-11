from django.core.mail import send_mass_mail
from django.core.mail import send_mail, BadHeaderError
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from spo.models import SendEmailInfo
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from spo.serializers import SendEmailSerializers
from smtplib import SMTPException


class SendEmail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        to_email = []
        try:
            title = data['title']
            content = data['content']
            from_email = data['from_email']
            for i in data['to_email']:
                to_email.append(i)

        except ParseError:
            return Response({'msg': '参数错误'}, status=ParseError.status_code)
        # send只发一条,成功返回1失败是0
        try:
            send_mail(subject=title, message=content, from_email=from_email,
                      recipient_list=to_email, fail_silently=False)
            serializers = SendEmailSerializers(data=data)
            if serializers.is_valid(raise_exception=True):
                serializers.save()
                return Response({
                    'msg': '发送邮件成功',
                })
        except BadHeaderError:
            return Response({
                'msg': 'Invalid header found.'
            })
        except SMTPException:
            data['status'] = 'n'
            serializers = SendEmailSerializers(data=data)
            if serializers.is_valid(raise_exception=True):
                serializers.save()
                return Response({
                    'msg': '发送邮件失败',
                })
