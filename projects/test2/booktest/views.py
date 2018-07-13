# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.conf import settings
from django.shortcuts import render,redirect
from models import *
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.paginator import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from task import *
# Create your views here.

def index(request):
    #heroinfo__hcontent_contains='adsf'
    list = BookInfo.books1.filter(Q(pk__gt=2)|Q(btitle__contains='a'))
    context ={'list':list}
    return render(request,'booktest/index.html',context)

def detail(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))
# 展示链接的页面
def getTest1(request):
    return render(request,'booktest/getTest1.html')
# 接受一键一值的情况
def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1,'b':b1,'c':c1}
    return render(request,'booktest/getTest2.html',context)
# 接受一键多值的情况
def getTest3(request):
    return render(request,'booktest/getTest3.html')

def postTest1(request):
    return render(request,'booktest/postTest1.html')

def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST.get('ugender')
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/postTest2.html',context)
def cookieTest(request):
    response =HttpResponse()
    cookie = request.COOKIES
    if cookie.has_key('t1'):
        response.write(cookie['t1'])
    # response.set_cookie('ti','abc')
    return response
def redTest1(request):
    # return HttpResponseRedirect('/booktest/redTest2/')
    return redirect('/booktest/redTest2/')
def redTest2(request):
    return HttpResponse('这是转向来的页面')

def session1(request):
    uname =request.session.get('myname','未登录')#'XXX'
    context = {'uname':uname}
    return render(request,'booktest/session1.html',context)

def session2(request):
    return render(request,'booktest/session2.html')

def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    # request.session.set_expiry(10)
    return redirect('/booktest/session1/')

def session3(request):
    #删除session
    del request.session['myname']
    return redirect('/booktest/session1/')

def show(request,id):
    context = {'id':id}
    return render(request,'booktest/show.html',context)

def index2(request):
    return render(request,'booktest/index2.html')

def user1(request):
    return render(request,'booktest/user1.html')
def user2(request):
    return render(request,'booktest/user2.html')

def htmlTest(request):
    context={'t1':'<h1>asd</h1>'}
    return render(request,'booktest/htmlTest.html',context)

def csrf1(request):
    return render(request,'booktest/csrfTest.html')

def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)

def verifyCode(request):
    from PIL import Image,ImageDraw,ImageFont
    import random
    # 创建背景色
    bgcolor = (random.randrange(50,100),random.randrange(50,100),random.randrange(50,100))

    width = 100
    height = 100
    image = Image.new('RGB',(width,height),bgcolor)
    font = ImageFont.truetype('FreeMono.ttf',24)
    draw =ImageDraw.Draw(image)
    text='ABCD01354sdf'
    texttemp =''
    for i in range(4):
        texttemp1=text[random.randrange(0,len(text))]
        texttemp +=texttemp1
        draw.text((i*25,0),
                  texttemp1,
                  (255,255,255),
                  font)
    request.session['code']=texttemp
    # for t1 in text:
    draw.text((0,0),text,(255,255,255),font)
    import cStringIO
    buf = cStringIO.StringIO()
    image.save(buf,'png')
    return HttpResponse(buf.getvalue(),'image/png')

def pic(request):
    return render(request,'booktest/pic.html')

def myExp(request):
    a = int('adg')
    return HttpResponse('hello')

def uploadPic(request):
    return render(request,'booktest/uploadPic.html')

def uploadHandle(request):
    f1 = request.FILES['pic1']
    fname = os.path.join(settings.MEDIA_ROOT,f1.name)
    with open(fname,'w') as f:
        for c in f1.chunks():
            f.write(c)
    return HttpResponse('<img src="/static/media/%s">'%f1.name)

def herolist(request,p1):
    if p1 == '':
        p1 = 1
    list = HeroInfo.objects.all()
    pagenatior = Paginator(list,5)
    page = pagenatior.page(int(p1))
    context = {'page':page}
    return render(request,'booktest/herolist.html',context)

def area(request):
    return render(request,'booktest/area.html')

def pro(request):
#     id1 = int(id)
#     if id1 == 0:
#         data = AreaInfo.objects.filter(parea__isnull=True)
#     else:
#         data = [{}]

    prolist = AreaInfo.objects.filter(parea__isnull=True)
    list = []
    for pro in prolist:
        list.append([pro.id,pro.title])
    return JsonResponse({'data':list})

def city(request,id):
    citylist = AreaInfo.objects.filter(parea__id=id)
    list=[]
    for item in citylist:
        list.append({'id':item.id,'title':item.title})

    return JsonResponse({'data':list})

def dis(request,id):
    citylist = AreaInfo.objects.filter(parea__id=id)
    list=[]
    for item in citylist:
        list.append({'id':item.id,'title':item.title})

    return JsonResponse({'data':list})

def htmlEditor(request):
    return render(request,'booktest/htmlEditor.html')

def htmlEditorHandle(request):
    html = request.POST['hcontent']
    test1 = Test1.objects.get(pk=1)
    test1.content=html
    test1.save()
    content = {'content':html}
    return render(request,'booktest/htmlshow.html',content)


# 缓存
@cache_page(60*10)
def cache1(request):
    return HttpResponse('hello1')

def cache2(request):
    return render(request,'booktest/cache.html')

def cache3(request):
    cache.set('key1','value1','600')
    # print(cache.get('key1'))
    # cache.clear() 清除缓存
    return HttpResponse("cache example")

def mysearch(request):
    return render(request,'booktest/mysearch.html')

def celeryTest(request):
    # shows()
    shows.delay()
    return HttpResponse('ok')