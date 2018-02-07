# -*- coding: utf-8 -*-

from django.http import HttpResponse
from model.models import *
from app01.models import Users
from app02.models import User
# 数据库操作
def testdb(request):
    Test(name='hahr33333ha').save()
    return HttpResponse("<p>数据添加成功！</p>")


def app01(request):
    Users(username='app013333', password='app01pass', age=20).save()
    return HttpResponse("<p>app01数据添加成功！</p>")


def app02(request):
    User(name='app02', passwd='app02222pass').save()
    return HttpResponse("<p>app02数据添加成功！</p>")


