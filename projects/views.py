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
from markdown import serializers
from rest_framework.viewsets import ModelViewSet
# from projects.serializer import ProjectsModelSerialzer

from projects.serializer import ProjectsSerialzer
import json

from projects.models import Project






class ProjectList(View):
    def get(self,request):
        #1,从数据库中获取所有项目
        project_qs = Project.objects.all()

        #2.将数据库模型类实例转换为字典类型（嵌套字典的列表）
        # project_list=[]
        # for project in project_qs:
        #     # one_dic ={
        #     #     'name':project.name,
        #     #     'leader':project.leader,
        #     #     'tester':project.tester,
        #     #     'programmer':project.programer,
        #     #     'publish_app':project.publish_app,
        #     #     'desc':project.desc
        #     # }
        #     project_list.append({
        #         'name': project.name,
        #         'leader': project.leader,
        #         'tester': project.tester,
        #         'programer': project.programer,
        #         'publish_app': project.publish_app,
        #         'desc': project.desc
        #     })
            #JsonResponse第一个参数默认只能为dict字典，如果要设为其他类型，需要将safe=Flase
        #如果返回的是列表数据（多条数据时），那么需要添加many=True
        serializer = ProjectsSerialzer(instance=project_qs,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self,request):
        '''
        新增项目
        :param request:
        :return:
        1、从前端获取json格式的数据，转换为python格式的类型
        为了严谨性，需要做各种复杂的校验
        比如：是否为json,c传递的项目数据是否符合要求，有些必传参数是否携带等
        '''
        json_data = request.body.decode('UTF-8')
        python_data = json.loads(json_data,encoding='UTF-8')

        serializer = ProjectsSerialzer(data=python_data)

        #校验前端输入的数据
        #1.调用序列化器对象的is_vaild方法，开始校验前端参数,
        #2.如果校验成功，返回true,反之则返回false
        #3.raise_exception=True,校验失败以后，会抛出异常
        #4.当调用is_valid方法之后，才可以调用errors属性，获取校验的错误提示（字典）
        #校验成功后，可以使用validated_data属性来获取
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors )
        #2。向数据库中新增项目
        # project = Project.objects.create(name=python_data['name'],
        #                        leader=python_data['leader'],
        #                         tester=python_data['tester'],
        #                        programer=python_data['programmr'],
        #                        publish_app=python_data['publish_app'],
        #                        desc=python_data['desc']
        #                        )
        # project = Project.objects.create(**serializer.validated_data)
        #1.如果在创建序列化对象的时候只给data传参，那么调用sava()方法
        #实际调用的就序列化器对象的Create（）方法
        # serializer.save(user='古鹰',age=16)
        serializer.save()
        #3.将模型类对象，转换为字典
        # one_dict = {
        #         'name': project.name,
        #         'leader':project.leader,
        #         'tester':project.tester,
        #         'programer':project.programer,
        #         'publish_app':project.publish_app,
        #         'desc':project.desc
        # }

        # serializer = ProjectsSerialzer(instance=project)
        return JsonResponse(serializer.data,safe=False,status=201)

class ProjectDetail(View):
    def get_object(self,pk):
        try:
            return  Project.objects.get(id=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        #1.校验前端传递的pk（项目ID）值，类型是否正确（正整数），在数据库中是否存在等
        #省略
        #2.获取指定PK值的项目
        project =self.get_object(pk)
        #3.将模型类对象转换为字典
        # one_dict = {
        #     'name': project.name,
        #     'leader': project.leader,
        #     'tester': project.tester,
        #     'programer': project.programer,
        #     'publish_app': project.publish_app,
        #     'desc': project.desc
        # }

        #通过模型类对象（或者查询集），传给instance可进行序列化操作
        serializer=ProjectsSerialzer(instance=project)
        return JsonResponse(serializer.data)

    def put(self,request,pk):
        # 1.校验前端传递的pk（项目ID）值，类型是否正确（正整数），在数据库中是否存在等
        # 省略
        # 2.获取指定PK值的项目


        project = self.get_object(pk)
        #3.从前端获取json格式的数据
        # 为了严谨性，需要做各种复杂的校验
        # 比如：是否为json, c传递的项目数据是否符合要求，有些必传参数是否携带等
        json_data = request.body.decode('UTF-8')
        python_data = json.loads(json_data, encoding='UTF-8')
        serializer = ProjectsSerialzer(instance=project,data=python_data)
        # serializer = ProjectsSerialzer(data=python_data)
        # serializer.is_valid(raise_exception=True)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors )
        #4.更新项目
        #在创建序列化器对象时，如果同时给instance和data传参
        #那么调用save（）方法，会自动调用序列化器的update
        serializer.save()

        # project.name = serializer.validated_data['name']
        # project.leader = serializer.validated_data['leader']
        # project.programer = serializer.validated_data['programer']
        # project.publish_app = serializer.validated_data['publish_app']
        # project.desc = serializer.validated_data['desc']

        # project.save()
        # 3.将模型类对象转换为字典
        # one_dict = {
        #     'name': project.name,
        #     'leader': project.leader,
        #     'tester': project.tester,
        #     'programer': project.programer,
        #     'publish_app': project.publish_app,
        #     'desc': project.desc
        # }

        # serializer = ProjectsSerialzer(instance=project)
        return JsonResponse(serializer.data,status=201)

    def delete(self,request,pk):
        # 1.校验前端传递的pk（项目ID）值，类型是否正确（正整数），在数据库中是否存在等
        # 省略
        # 2.获取指定PK值的项目
        project = self.get_object(pk)
        project.delete(project)
        return JsonResponse(None,safe=False,status=204)

# class ProjectViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectsModelSerialzer









