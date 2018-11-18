# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Task,ReleaseInfo

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id', 'title', 'description', 'completed', 'create_date')

class ReleaseInfoSerializer(serializers.ModelSerializer):
	class  Meta:
		model = ReleaseInfo
		fields = ('id','status','application_id','env','subenv','started_at','finished_at')
		# fields = "__all__"
# class ReleaseInfoSerializer(serializers.Serializer):
