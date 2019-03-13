"""django_start URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from rest_framework.schemas import get_schema_view

from webdriver_service.django_start.django_start.view import changeModel, changeModelBatch
from webdriver_service.django_start.manage import hello
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

# 视图
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    '''查看，编辑用户的界面'''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    '''查看，编辑组的界面'''
    queryset = Group
    serializer_class = GroupSerializer


# 路由
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'groups', GroupViewSet, base_name='group')

# 重要的是如下三行
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    url(r"test.go", hello),
    url(r"fapiao.go", changeModel),
    url(r"zhongdeng.go", changeModel),
    url(r"zhongdengdengji.go", changeModel),
    url(r"fapiaoList.go", changeModelBatch),
    # API文档接口路由
    # swagger接口文档路由
    url(r'^docs/', schema_view, name="docs"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # drf登录
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
