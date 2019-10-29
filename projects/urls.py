"""LearnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
# from projects.views import index
from projects import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers

#1.创建SimpleRouter路由对象
router = routers.SimpleRouter()
# router = routers.DefaultRouter()

#2.注册路由,第一个参数prefix为路由前缀，一般添加为应用名即可，
#第二个参数viewset为视图集，不加as_view
router.register(r'projects',views.ProjectsViewSet)


#全局路由配置
#1、每个应用（模块）都会维护一个子路由（当前应用的路由信息）
#2、跟主路由一样，也是从上到下进行匹配
#3、能匹配上则执行path第二个参数指定的视图，匹配不上，则抛出404异常
# router = DefaultRouter()
# router.register(r'projects',views.ProjectViewSet)
urlpatterns = [
    #3.将自动生产的路由添加到这个urlpatterns列表中
    # path('',include(router.urls)),

     #如果为类视图，path第二个参数为类视图名.as_view()
     # path('', views.IndexView.as_view()),
    # path('index/',index),
    #  path('<int:pk>/',views.IndexView.as_view())
     #int为路径参数类型转换器
     #：左边为转换器，右边为参数名
     #int,slug,uuid,
     # path('projects/',views.ProjectList.as_view()),
     # path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('projects/',views.ProjectsViewSet.as_view({
        'get':'list',
        'post':'create',
    }),name='projects_list'),

    path('projects/<int:pk>/', views.ProjectsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete':'destroy',
    })),
    path('projects/names/',views.ProjectsViewSet.as_view({
            'get':'names',

        }),name='projects_names'),

    path ( 'projects/<int:pk>/interfaces/', views.ProjectsViewSet.as_view ( {
        'get': 'interfaces',

    } ) ),


]
# urlpatterns += router.urls
