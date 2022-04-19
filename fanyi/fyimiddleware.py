#自定义中间件类，（执行登录判断）
from  django.shortcuts import redirect
from  django.urls import  reverse
import re

class ShopMIddleware:
    def __init__(self,get_response):
        self.get_response=get_response

        print('ShopMIddleware')

    def __call__(self,request):
        path=request.path
        print(path)
        if re.match('^/',path):
            if 'oldText' in request.session:
                del request.session['oldText']

        response = self.get_response(request)


        return response