from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from spo.serializers import TaskSerializers
from spo.models import Task, TestCase
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status


class AddTask(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            serializer = TaskSerializers(data=request.data)
        except ParseError:
            return Response({
                'msg', 'ParseError '
            }, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'code': Response.status_code,
                'message': 'Add Success',
                'task_id': serializer.data.get('id')
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class TaskList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            obj_task = Task.objects.get(pk=pk)
            serializer = TaskSerializers(obj_task)
        else:
            queryset = Task.objects.all()
            serializer = TaskSerializers(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EditTask(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def push(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            obj_task = Task.objects.get(pk=pk)
            data = request.data
        except ParseError:
            return Response({
                'msg', 'ParseError '
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = TaskSerializers(instance=obj_task, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'task_id': serializer.data.get('id'),
                'msg': 'success'
            }, status=status.HTTP_200_OK)


class DelTask(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, **kwargs):
        pk = kwargs.get('pk')
        try:
            obj_task = Task.objects.get(pk=pk)
        except ParseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if obj_task.delect():
            return Response({
                'msg': 'Delete Success',
                'task_id': pk
            }, status=status.HTTP_200_OK)
