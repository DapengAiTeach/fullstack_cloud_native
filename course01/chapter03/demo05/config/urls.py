from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def hello(request):
    print("hello路径被访问了")
    return HttpResponse("你好，张老师！")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
]
