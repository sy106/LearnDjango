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
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="sy106 API接口文档平台",    # 必传
#         default_version='v1',   # 必传
#         description="这是一个美轮美奂的接口文档",
#         terms_of_service="http://api.keyou.site",
#         contact=openapi.Contact(email="sy106@126.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     # permission_classes=(permissions.AllowAny,),   # 权限类
# )
#
# #全局路由配置
# #1、urlpatterns是固定名称列表
# #2、列表中的一个元素，就代表一条路由
# #3、从上到下进行匹配，如果匹配上，django会导入和调用path函数第二个参数指定的视图，或者去子路由中去匹配
# #4、如果匹配不上，会自动抛出一个404异常（默认为404页面，状态码是404）
# urlpatterns = [
#     path ( 'admin/', admin.site.urls ),
#     path ( '', include ( 'projects.urls' ) ),
#     path ( 'docs/', include_docs_urls ( title = '测试平台接口文档',
#                                         description = '这是一个美轮美奂的接口文档平台' ) ),
#
#     re_path ( r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui ( cache_timeout = 0 ),
#               name = 'schema-json' ),
#     path ( 'swagger/', schema_view.with_ui ( 'swagger', cache_timeout = 0 ), name = 'schema-swagger-ui' ),
#     path ( 'redoc/', schema_view.with_ui ( 'redoc', cache_timeout = 0 ), name = 'schema-redoc' ),
#
#     path ( 'api/', include ( 'rest_framework.urls' ) ),
#
#     path ( 'user/', include ( 'user.urls' ) ),
# ]
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Lemon API接口文档平台",    # 必传
        default_version='v1',   # 必传
        description="这是一个美轮美奂的接口文档",
        terms_of_service="http://api.keyou.site",
        contact=openapi.Contact(email="keyou100@qq.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),   # 权限类
)

urlpatterns = {
    path ( 'admin/', admin.site.urls ),
    path ( '', include ( 'projects.urls' ) ),
    path ( 'docs/', include_docs_urls ( title = '测试平台接口文档',
                                        description = '这是一个美轮美奂的接口文档平台' ) ),

    re_path ( r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui ( cache_timeout = 0 ),
              name = 'schema-json' ),
    path ( 'swagger/', schema_view.with_ui ( 'swagger', cache_timeout = 0 ), name = 'schema-swagger-ui' ),
    path ( 'redoc/', schema_view.with_ui ( 'redoc', cache_timeout = 0 ), name = 'schema-redoc' ),

    path ( 'api/', include ( 'rest_framework.urls' ) ),

    path ( 'user/', include ( 'user.urls' ) ),
}
