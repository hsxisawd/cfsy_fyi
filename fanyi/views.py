from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from fanyi.models import fyi
import requests
import hashlib,time,random

def md5_sgin(text):
    hl=hashlib.md5()
    sgin_text='6key_cibaifanyicjbysdlove1'+text
    hl.update(sgin_text.encode(encoding='utf-8'))
    sign=hl.hexdigest()[0:16]
    return sign,text

def fanyi(sign,text,ol,nl):
    url=f"http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign={sign}"
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}
    p={'from': ol,'to': nl,'q': text}
    time.sleep(random.randint(1,2))
    js_data=requests.post(url,data=p,headers=header).json()
    context={"out":js_data['content']['out']}
    return context

def Fyi(request):
    fy=fyi.objects.all()
    a = []
    for i in fy:
        a.append(i.toDict())
    request.session['fy']=a
    return render(request, 'text.html')

def mian(request):

        oldlanguage=request.POST['s1']
        text=request.POST['oldtext']
        newlanguage = request.POST['s2']
        if  text !='':
            request.session["oldText"]=text
            a,b=md5_sgin(text)
            context=fanyi(a,b,oldlanguage,newlanguage)
            return render(request, 'text.html', context)
        return render(request,'text.html')