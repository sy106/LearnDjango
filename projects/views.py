# from django.db.models import Q
# from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
# from django.views import View
# from projects.models import Project
#
# # Create your views here.
# #函数视图
# #视图函数第一个参数
# #request是HttpRequest的对象，包含前端用户的所有请求信息
# def index(request):
#     """
#     :parameter request:是HttpRequest的对象，包含前端用户的所有请求信息
#     :return:必须返回一个HttpRequest的对象或者子对象
#     """
#     if request.method == "POST":
#         return HttpResponse("<h1>POST请求:Hello,python!</h1>")
#     elif request.method == "GET":
#         return HttpResponse("<h1>GET请求:Hello,python!</h1>")
#     else:
#         return  HttpResponse("<h1>其他请求：Hello,python!</h1>")
#     #类视图
# class IndexView(View):
#     """
#     index主页类视图
#     """
#     # def get(self,request):
#     #     #get 请求
#     #     #1\使用request.GET来获取查询字符串参数
#     #     #2、request.GET返回的是一个 字典类的对象，支持字典中的所有操作
#     #     #3、查询字符串参数中，如果有使用多个相同的key,使用request.GET获取的是最后一个值
#     #     #4、使用request.GET.getlist('name')可以获取多个相同key值的参数
#     #     return HttpResponse("<h1>GET请求:Hello,python!</h1>")
#         #从数据库中读取数据
#         # datas =[
#         #     {
#         #         'project_name':'前程贷项目',
#         #         'leader':'可优',
#         #         'app_name':'P2P平台应用'
#         #     },
#         #     {
#         #         'project_name': '探索火星项目',
#         #         'leader': '优优',
#         #         'app_name': '吊炸天项目'
#         #     },
#         #     {
#         #         'project_name': '务必牛逼的项目',
#         #         'leader': '可可',
#         #         'app_name': '神秘应用'
#         #     },
#         # ]
#         # return  render(request,'index.html',locals())
#     def get(self,request):
#         # datas={
#         #         'name':'yanyan',
#         #         'age':18
#         #     }
#         #创建数据
#         #方法1：创建模型类对象
#         #方法2：保存对象
#         # one_prj=Project(name='这是一个牛逼的项目',leader='icon',programer='若言',publish_app='这是一个厉害的应用',desc='无描述')
#         #调用save方法保存，才去数据库中执行SQL
#         # one_prj.save()
#         # pass
#         # Project.objects.create(name='这是一个牛逼的项目5210',leader='icon111',programer='若言5210',publish_app='这是一个厉害的应用5210',desc='无描述5210')
#         # 获取某一个指定得记录，get(),get方法只能返回一条记录，返回多条会报异常
#         # one_prj = Project.objects.get(id=1)
#         #获取多条记录，用filter()或者exclude（）,使用filter是返回满足条件得queryset，exclude是返回不满足查询条件得查询集
#         # qs=Project.objects.filter(id=1)
#         #4、关联查询
#         #外键查询，外键字段__从表得字段名__
#         # qs = Project.objects.filter(interfaces__name='登录接口')
#         # qs = Project.objects.filter(leader='icon',name__contains='牛逼')
#         #可以使用Q变量指定多个条件，那么条件之间是或的关系
#         #7、查询集的操作
#         #查询集相当于一个列表，支持列表中的大多数操作（通过数字正向索引获取值，正向切片，for）
#         #查询集是对数据库操作的一种优化
#         #查询集会缓存结果
#         #查询集还支持链式操作
#         qs = Project.objects.filter(Q(leader='icon') | Q(name_contains='牛逼'))
#         qs.filter().filter().filter()
#         return HttpResponse("<h1>GET请求:Hello,python!</h1>")
#
#
#         # return JsonResponse( )
#
#     def post(self, request):
#         # 1\使用request.POST['age']来获取 www-form表单参数
#
#         return HttpResponse("<h1>POST请求:Hello,python!</h1>")
#     def put(self,request):
#         #get 请求
#         return HttpResponse("<h1>PUT请求:Hello,python!</h1>")
#     def delete(self,request):
#         #get 请求
#         qs_d = Project.objects.filter(id=1)
#         qs_d.delete()
#         return HttpResponse("<h1>Del请求:Hello,python!</h1>")
#



from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from markdown import serializers
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework  import status,filters

from rest_framework.viewsets import ModelViewSet
# from projects.serializer import ProjectsModelSerialzer

from projects.serializer import ProjectsModelSerialzer,\
    ProjectNameSerializer,InterfacesByProjectIdSerializer
import json

from projects.models import Project

from utils.pagination import PageNumberPaginationManual
from rest_framework import mixins,generics







# class ProjectList(generics.ListCreateAPIView):
#
#     #1.指定查询集
#     queryset = Project.objects.all()
#     #2.指定序列化器
#     serializer_class = ProjectsModelSerialzer
#     # 3.在视图类中指定过滤引擎
#     # filter_backends = [filters.OrderingFilter]
#     # 4.指定需要排序的字段
#     ordering_fileds = ['name', 'leader']
#     #在类视图中指定过滤引擎
#     # filter_backends = [DjangoFilterBackend]
#     #6.指定需要过滤的字段
#     filterset_fileds = ['name', 'leader','tester']
#     #7.在某个视图中指定分页类
#     # pagination_class = PageNumberPaginationManual
#     # def get(self,request,*args,**kwargs):
#     #     #1,从数据库中获取所有项目
#     #     # project_qs = Project.objects.all()
#     #
#     #     #2.将数据库模型类实例转换为字典类型（嵌套字典的列表）
#     #     # project_list=[]
#     #     # for project in project_qs:
#     #     #     # one_dic ={
#     #     #     #     'name':project.name,
#     #     #     #     'leader':project.leader,
#     #     #     #     'tester':project.tester,
#     #     #     #     'programmer':project.programer,
#     #     #     #     'publish_app':project.publish_app,
#     #     #     #     'desc':project.desc
#     #     #     # }
#     #     #     project_list.append({
#     #     #         'name': project.name,
#     #     #         'leader': project.leader,
#     #     #         'tester': project.tester,
#     #     #         'programer': project.programer,
#     #     #         'publish_app': project.publish_app,
#     #     #         'desc': project.desc
#     #     #     })
#     #         #JsonResponse第一个参数默认只能为dict字典，如果要设为其他类型，需要将safe=Flase
#     #     #如果返回的是列表数据（多条数据时），那么需要添加many=True
#     #     #5.使用get_queryset（）获取查询集
#     #     # project_qs = self.get_queryset()
#     #     #6.使用filter_queryset方法过滤查询
#     #     # project_qs = self.filter_queryset(self.get_queryset())
#     #     # #使用paginate_queryset来进行分页，然后返回分页之后的查询集
#     #     # page = self.paginate_queryset(project_qs)
#     #     # if page is not None:
#     #     #     serializer = self.get_serializer(instance=project_qs, many=True)
#     #     #     #可以get_paginated_response返回
#     #     #     return self.get_paginated_response(serializer.data)
#     #     # serializer = self.get_serializer(instance=project_qs,many=True)
#     #     # return Response(serializer.data)
#     #     return self.list(self,request,*args,**kwargs)#首先继承mixin,然后继承再继承GenericAPIView
#
#     # def post(self,request,*args,**kwargs):
#     #     '''
#     #     新增项目
#     #     :param request:
#     #     :return:
#     #     1、从前端获取json格式的数据，转换为python格式的类型
#     #     为了严谨性，需要做各种复杂的校验
#     #     比如：是否为json,c传递的项目数据是否符合要求，有些必传参数是否携带等
#     #     '''
#     #     # json_data = request.body.decode('UTF-8')
#     #     # python_data = json.loads(json_data,encoding='UTF-8')
#     #
#     #     # serializer = ProjectsModelSerialzer(data=python_data)
#     #
#     #     #当视图继承APIView
#     #     #请求实例方法中，第二个参数request为Request对象，是对Django中HTTPRequest对象进行了扩展
#     #     # serializer = ProjectsModelSerialzer(data=request.data)
#     #     #
#     #     # #校验前端输入的数据
#     #     # #1.调用序列化器对象的is_vaild方法，开始校验前端参数,
#     #     # #2.如果校验成功，返回true,反之则返回false
#     #     # #3.raise_exception=True,校验失败以后，会抛出异常
#     #     # #4.当调用is_valid方法之后，才可以调用errors属性，获取校验的错误提示（字典）
#     #     # #校验成功后，可以使用validated_data属性来获取
#     #     # try:
#     #     #     serializer.is_valid(raise_exception=True)
#     #     # except Exception as e:
#     #     #     return Response(serializer.errors)
#     #     # #2。向数据库中新增项目
#     #     # # project = Project.objects.create(name=python_data['name'],
#     #     # #                        leader=python_data['leader'],
#     #     # #                         tester=python_data['tester'],
#     #     # #                        programer=python_data['programmr'],
#     #     # #                        publish_app=python_data['publish_app'],
#     #     # #                        desc=python_data['desc']
#     #     # #                        )
#     #     # # project = Project.objects.create(**serializer.validated_data)
#     #     # #1.如果在创建序列化对象的时候只给data传参，那么调用sava()方法
#     #     # #实际调用的就序列化器对象的Create（）方法
#     #     # # serializer.save(user='古鹰',age=16)
#     #     # serializer.save()
#     #     # #3.将模型类对象，转换为字典
#     #     # # one_dict = {
#     #     # #         'name': project.name,
#     #     # #         'leader':project.leader,
#     #     # #         'tester':project.tester,
#     #     # #         'programer':project.programer,
#     #     # #         'publish_app':project.publish_app,
#     #     # #         'desc':project.desc
#     #     # # }
#     #     #
#     #     # # serializer = ProjectsSerialzer(instance=project)
#     #     # return Response(serializer.data,status=201)
#     #     return self.create(request,*args,**kwargs)
#1.需要继承GenericAPIView基类

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions

#APIView,GenericView
#ViewSet不再支持get,post,put,delete等请求方法，只支持action动作
#但ViewSet中未提供get_serializer（），get_object()等方法
#所以需要继承GnericAPIView
# class ProjectsViewSet(viewsets.GenericViewSet,
#                       mixins.ListModelMixin,
#                       mixins.DestroyModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.CreateModelMixin):
class ProjectsViewSet(viewsets.ModelViewSet):
    """
    create:
    创建项目

    retrieve:
    获取项目详情数据

    update:
    完整更新项目

    partial_update:
    部分更新项目

    destroy:
    删除项目

    list:
    获取项目列表数据

    names:
    获取所有项目名称

    interfaces:
    获取指定项目的所有接口数据
    """
    queryset = Project.objects.all()
    serializer_class = ProjectsModelSerialzer
    ordering_fileds = ['name', 'leader']
    filterset_fileds = ['name', 'leader', 'tester']

    permission_classes = [ permissions.IsAuthenticated ]

    #1.可以使用action装饰器来声明自定义的动作
    #默认情况下，实例方法名就是动作名
    #methods参数用于指定该动作支持的请求方法,默认是get
    #detail参数用于指定该动作要处理的是否为详情资源对象（URL是否需要传递PK键值）
    @action ( methods = [ 'get' ],detail = False)
    def names(self,request,*args,**kwargs):
        queryset=self.get_queryset()
        serializer = ProjectNameSerializer(instance = queryset,many = True)
        return Response(serializer.data)

    @action (detail = False )
    def interfaces(self, request,*args,**kwargs):
        instance=self.get_object()
        serializer = InterfacesByProjectIdSerializer(instance = instance)
        return Response(serializer.data)


    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
    #
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED )


# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
#     #2.必须指定queryset和serilizer_class
#     #1.queryset用于指定需要使用的查询集
#     queryset = Project.objects.all()
#     #2.serializer_class指定需要用到的序列化器类
#     serializer_class = ProjectsModelSerialzer
#     #使用lookup_field类属性，可以修改主键路由名称
#     #lookup_field='id'
#
#     # def get_object(self,pk):
#     #     try:
#     #         return  Project.objects.get(id=pk)
#     #     except Project.DoesNotExist:
#     #         raise Http404
#
#     # def get(self,request,*args,**kwargs):
#     #     #1.校验前端传递的pk（项目ID）值，类型是否正确（正整数），在数据库中是否存在等
#     #     #省略
#     #     #2.获取指定PK值的项目
#     #     #使用get_object（）方法，返回详情视图所需要的模型类对象
#     #     # project =self.get_object()
#     #     # #3.将模型类对象转换为字典
#     #     # # one_dict = {
#     #     # #     'name': project.name,
#     #     # #     'leader': project.leader,
#     #     # #     'tester': project.tester,
#     #     # #     'programer': project.programer,
#     #     # #     'publish_app': project.publish_app,
#     #     # #     'desc': project.desc
#     #     # # }
#     #     #
#     #     # #通过模型类对象（或者查询集），传给instance可进行序列化操作
#     #     # # serializer=ProjectsModelSerialzer(instance=project)
#     #     # #使用get_serializer获取序列化器类
#     #     # serializer = self.get_serializer(instance=project)
#     #     # # return JsonResponse(serializer.data)
#     #     # return  Response(serializer.data,status=status.HTTP_200_OK)
#     #     return self.retrieve(request,*args,**kwargs)
#     #
#     # def put(self,request,*args,**kwargs):
#     #     # 1.校验前端传递的pk（项目ID）值，类型是否正确（正整数），在数据库中是否存在等
#     #     # 省略
#     #     # 2.获取指定PK值的项目
#     #
#     #
#     #     # project = self.get_object()
#     #     # #3.从前端获取json格式的数据
#     #     # # 为了严谨性，需要做各种复杂的校验
#     #     # # 比如：是否为json, c传递的项目数据是否符合要求，有些必传参数是否携带等
#     #     # # json_data = request.body.decode('UTF-8')
#     #     # # python_data = json.loads(json_data, encoding='UTF-8')
#     #     # # serializer = ProjectsModelSerialzer(instance=project,data=python_data)
#     #     # serializer = self.get_serializer(instance=project, data=request.data)
#     #     # # serializer = ProjectsSerialzer(data=python_data)
#     #     # # serializer.is_valid(raise_exception=True)
#     #     #
#     #     # try:
#     #     #     serializer.is_valid(raise_exception=True)
#     #     # except Exception as e:
#     #     #     return Response(serializer.errors)
#     #     #4.更新项目
#     #     #在创建序列化器对象时，如果同时给instance和data传参
#     #     #那么调用save（）方法，会自动调用序列化器的update
#     #     # serializer.save()
#     #
#     #     # project.name = serializer.validated_data['name']
#     #     # project.leader = serializer.validated_data['leader']
#     #     # project.programer = serializer.validated_data['programer']
#     #     # project.publish_app = serializer.validated_data['publish_app']
#     #     # project.desc = serializer.validated_data['desc']
#     #
#     #     # project.save()
#     #     # 3.将模型类对象转换为字典
#     #     # one_dict = {
#     #     #     'name': project.name,
#     #     #     'leader': project.leader,
#     #     #     'tester': project.tester,
#     #     #     'programer': project.programer,
#     #     #     'publish_app': project.publish_app,
#     #     #     'desc': project.desc
#     #     # }
#     #
#     #     # serializer = ProjectsSerialzer(instance=project)
#     #     # return Response(serializer.data,status=201)
#     #     return self.update(request,*args,**kwargs)
#     #
#     # def delete(self,request,*args,**kwargs):
#     #     # 1.校验前端传递的pk（项目ID）值，类型是否正确（正整数），在数据库中是否存在等
#     #     # 省略
#     #     # 2.获取指定PK值的项目
#     #     # project = self.get_object()
#     #     # project.delete(project)
#     #     # return Response(None,status=204)
#     #     return self.delete(request,*args,**kwargs)
#
# # class ProjectViewSet(ModelViewSet):
# #     queryset = Project.objects.all()
# #     serializer_class = ProjectsModelSerialzer









