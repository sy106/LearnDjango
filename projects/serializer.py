#-*- coding:utf-8 -*-
# @Time     : 2019/10/18 10:52
# @Author   : shenyuan
# @Email    : shenyuan@suray.cn
# @File     : serializer.PY


from rest_framework.serializers import ModelSerializer
from projects.models import Project

class ProjectsModelSerialzer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

