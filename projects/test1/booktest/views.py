# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.http import *
# from django.template import RequestContext,loader
# Create your views here.

def index(request):
    # temp = loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    booklist=BookInfo.objects.all()
    contex ={'title':'Helllo'}
    contex1 = {'list':booklist}
    return render(request,'booktest/index.html',contex1)

def show(request,id):
    book= BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    context={'list':herolist}
    return render(request, 'booktest/show.html', context)
