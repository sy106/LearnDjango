from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

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
    def get(self,request):
        #get 请求
        #1\使用request.GET来获取查询字符串参数
        #2、request.GET返回的是一个 字典类的对象，支持字典中的所有操作
        #3、查询字符串参数中，如果有使用多个相同的key,使用request.GET获取的是最后一个值
        #4、使用request.GET.getlist('name')可以获取多个相同key值的参数
        return HttpResponse("<h1>GET请求:Hello,python!</h1>")
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

    def post(self, request):
        # get 请求
        return HttpResponse("<h1>POST请求:Hello,python!</h1>")
    def put(self,request):
        #get 请求
        return HttpResponse("<h1>PUT请求:Hello,python!</h1>")
    def delete(self,request):
        #get 请求
        return HttpResponse("<h1>Del请求:Hello,python!</h1>")

