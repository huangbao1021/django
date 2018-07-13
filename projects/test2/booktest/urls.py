from django.conf.urls import url
from django.contrib import admin
import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^(\d+)$', views.show,name='show'),
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)$',views.detail,name='detail'),
    url(r'^getTest1/$',views.getTest1),
    url(r'^getTest2/$',views.getTest2),
    url(r'^getTest3/$',views.getTest3),
    url(r'^postTest1/$', views.postTest1),
    url(r'^postTest2/$', views.postTest2),
    url(r'^cookieTest/$',views.cookieTest),
    url(r'^redTest1/$',views.redTest1),
    url(r'^redTest2/$',views.redTest2),
    url(r'^session1/$',views.session1),
    url(r'^session2/$',views.session2),
    url(r'^session2_handle/$',views.session2_handle),
    url(r'^session3/$',views.session3),
    url(r'^index2/$',views.index2),
    url(r'^user1/$',views.user1),
    url(r'^user2/$',views.user2),
    url(r'^htmlTest/$',views.htmlTest),
    url(r'^csrf1$',views.csrf1),
    url(r'^csrf2$',views.csrf2),
    url(r'^verify',views.verifyCode),
    url(r'^pic',views.pic),
    url(r'^myExp',views.myExp),
    url(r'^uploadPic/$',views.uploadPic),
    url(r'^uploadHandle/$',views.uploadHandle),
    url(r'^herolist/(\d*)',views.herolist),
    url(r'^area/$',views.area),
    url(r'^pro/$',views.pro),
    url(r'^city(\d+)',views.city),
    url(r'^dis(\d+)',views.dis),
    url(r'^htmlEditor/$',views.htmlEditor),
    url(r'^htmlEditorHandle/$',views.htmlEditorHandle),
    url(r'^cache1/$',views.cache1),
    url(r'^cache2/$',views.cache2),
    url(r'^cache3/$',views.cache3),
    url(r'^mysearch',views.mysearch),
    url(r'^celeryTest/$',views.celeryTest)
]