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

from django.urls import path
from projects.views import index
from projects import views


#全局路由配置
#1、每个应用（模块）都会维护一个子路由（当前应用的路由信息）
#2、跟主路由一样，也是从上到下进行匹配
#3、能匹配上则执行path第二个参数指定的视图，匹配不上，则抛出404异常

urlpatterns = [
     #如果为类视图，path第二个参数为类视图名.as_view()
     path('', views.IndexView.as_view()),
    # path('index/',index),

]
