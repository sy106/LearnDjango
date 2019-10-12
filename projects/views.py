from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from projects.models import Project

# Create your views here.
#函数视图
#视图函数第一个参数
#request是HttpRequest的对象，包含前端用户的所有请求信息
def index(request):
    """
    :parameter request:是HttpRequest的对象，包含前端用户的所有请求信息
    :return:必须返回一个HttpRequest的对象或者子对象
    """
    if request.method == "POST":
        return HttpResponse("<h1>POST请求:Hello,python!</h1>")
    elif request.method == "GET":
        return HttpResponse("<h1>GET请求:Hello,python!</h1>")
    else:
        return  HttpResponse("<h1>其他请求：Hello,python!</h1>")
    #类视图
class IndexView(View):
    """
    index主页类视图
    """
    # def get(self,request):
    #     #get 请求
    #     #1\使用request.GET来获取查询字符串参数
    #     #2、request.GET返回的是一个 字典类的对象，支持字典中的所有操作
    #     #3、查询字符串参数中，如果有使用多个相同的key,使用request.GET获取的是最后一个值
    #     #4、使用request.GET.getlist('name')可以获取多个相同key值的参数
    #     return HttpResponse("<h1>GET请求:Hello,python!</h1>")
        #从数据库中读取数据
        # datas =[
        #     {
        #         'project_name':'前程贷项目',
        #         'leader':'可优',
        #         'app_name':'P2P平台应用'
        #     },
        #     {
        #         'project_name': '探索火星项目',
        #         'leader': '优优',
        #         'app_name': '吊炸天项目'
        #     },
        #     {
        #         'project_name': '务必牛逼的项目',
        #         'leader': '可可',
        #         'app_name': '神秘应用'
        #     },
        # ]
        # return  render(request,'index.html',locals())
    def get(self,request):
        # datas={
        #         'name':'yanyan',
        #         'age':18
        #     }
        #创建数据
        #方法1：创建模型类对象
        #方法2：保存对象
        # one_prj=Project(name='这是一个牛逼的项目',leader='icon',programer='若言',publish_app='这是一个厉害的应用',desc='无描述')
        #调用save方法保存，才去数据库中执行SQL
        # one_prj.save()
        # pass
        # Project.objects.create(name='这是一个牛逼的项目5210',leader='icon111',programer='若言5210',publish_app='这是一个厉害的应用5210',desc='无描述5210')
        # 获取某一个指定得记录，get(),get方法只能返回一条记录，返回多条会报异常
        # one_prj = Project.objects.get(id=1)
        #获取多条记录，用filter()或者exclude（）,使用filter是返回满足条件得queryset，exclude是返回不满足查询条件得查询集
        # qs=Project.objects.filter(id=1)
        #4、关联查询
        #外键查询，外键字段__从表得字段名__
        # qs = Project.objects.filter(interfaces__name='登录接口')
        # qs = Project.objects.filter(leader='icon',name__contains='牛逼')
        #可以使用Q变量指定多个条件，那么条件之间是或的关系
        #7、查询集的操作
        #查询集相当于一个列表，支持列表中的大多数操作（通过数字正向索引获取值，正向切片，for）
        #查询集是对数据库操作的一种优化
        #查询集会缓存结果
        #查询集还支持链式操作
        qs = Project.objects.filter(Q(leader='icon') | Q(name_contains='牛逼'))
        qs.filter().filter().filter()
        return HttpResponse("<h1>GET请求:Hello,python!</h1>")


        # return JsonResponse( )

    def post(self, request):
        # 1\使用request.POST['age']来获取 www-form表单参数

        return HttpResponse("<h1>POST请求:Hello,python!</h1>")
    def put(self,request):
        #get 请求
        return HttpResponse("<h1>PUT请求:Hello,python!</h1>")
    def delete(self,request):
        #get 请求
        qs_d = Project.objects.filter(id=1)
        qs_d.delete()
        return HttpResponse("<h1>Del请求:Hello,python!</h1>")

