# -*- coding:utf-8 -*-
from django.db import models


class Task(models.Model):
    title = models.CharField('标题', max_length=100)
    description = models.TextField('描述')
    completed = models.BooleanField('是否完成', default=False)
    create_date = models.DateTimeField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.title



class ReleaseInfo(models.Model):
 
    status = models.CharField('status',max_length=100)
    application_id = models.CharField('application_id',max_length=100)
    env = models.CharField('env',max_length=100)
    subenv = models.CharField('subenv',max_length=100)
    started_at = models.CharField('started_at',max_length=100)
    finished_at = models.CharField('finished_at',max_length=100)
      

    # release = models.CharField('release',max_length=1000)

    def __unicode__(self):
        return self.application_id