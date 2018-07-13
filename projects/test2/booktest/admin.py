# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

# Register your models here.
class HeroInfoline(admin.TabularInline):
    model = HeroInfo
    extra = 3
# @admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 1
    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_date']})
    ]
    inlines = [HeroInfoline]

admin.site.register(BookInfo,BookInfoAdmin)

admin.site.register(HeroInfo)

admin.site.register(Test1)
