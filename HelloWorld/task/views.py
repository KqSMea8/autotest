# -*- coding:utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Task,ReleaseInfo
from .serializers import TaskSerializer,ReleaseInfoSerializer


from django.http import QueryDict
from rest_framework.request import Request
import json
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

def get_parameter_dic(request, *args, **kwargs):
    if isinstance(request, Request) == False:
        return {}

    query_params = request.query_params
    if isinstance(query_params, QueryDict):
        query_params = query_params.dict()
    result_data = request.data
    if isinstance(result_data, QueryDict):
        result_data = result_data.dict()

    if query_params != {}:
        return query_params
    else:
        return result_data

class RlsInfo(APIView):

    # coreapi_fields=(
    #     DocParam("token"),
    # )

    def get(self, request, *args, **kwargs):
        params=get_parameter_dic(request)
        return JsonResponse(data=params)

    def post(self, request, *args, **kwargs):
        params=get_parameter_dic(request)
        return JsonResponse(data=params)

    def put(self, request, *args, **kwargs):
        params=get_parameter_dic(request)
        return JsonResponse(data=params)




# 第一种方式：APIView
class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 第二种方式：通用视图 ListCreateAPIView
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# 第三种方式：装饰器 api_view
@api_view(['GET', 'POST'])
def task_list(request):
    '''
    List all tasks, or create a new task.
    '''
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def rlsinfo_list(request,format=None):
    '''
    List all tasks, or create a new task.
    '''
    # print(request.body)
    
    # print(request.data)

    if request.method == 'GET':
        rlsinfo = ReleaseInfo.objects.all()
        serializer = ReleaseInfoSerializer(rlsinfo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        rjd = json.loads(request.body)
        # print(rjd['release'])
        # print(rjd['release']['status'])
        # print(rjd['release']['application_id'])
        # print(rjd['release']['env'])
        # print(rjd['release']['subenv'])
        # print(rjd['release']['started_at'])
        # print(rjd['release']['finished_at'])
        # stream = BytesIO(rjd['release'])
        # rqd = JSONParser().parse(stream)
        # rqd = {'release':str(rjd['release'])}
        rqd = {}
        rqd['status'] = str(rjd['release']['status'])
        rqd['application_id'] = str(rjd['release']['application_id'])
        rqd['env'] = str(rjd['release']['env'])
        rqd['subenv'] = str(rjd['release']['subenv'])
        rqd['started_at'] = str(rjd['release']['started_at'])
        rqd['finished_at'] = str(rjd['release']['finished_at'])

        serializer = ReleaseInfoSerializer(data=rqd)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def rlsinfo_detail(request, pk,format=None):
    print(request.body)
    try:
        rlsinfo = ReleaseInfo.objects.get(pk=pk)
    except ReleaseInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReleaseInfoSerializer(rlsinfo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReleaseInfoSerializer(rlsinfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        rlsinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
