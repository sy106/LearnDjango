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
from django.contrib import admin
from django.urls import path,include
# from projects.views import index

#全局路由配置
#1、urlpatterns是固定名称列表
#2、列表中的一个元素，就代表一条路由
#3、从上到下进行匹配，如果匹配上，django会导入和调用path函数第二个参数指定的视图，或者去子路由中去匹配
#4、如果匹配不上，会自动抛出一个404异常（默认为404页面，状态码是404）
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/',index),
    path('',include('projects.urls')),
    path('api/',include('rest_framework.urls')),
]
