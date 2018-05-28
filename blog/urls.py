from django.conf.urls import url
from . import views

app_name = 'blog' #告诉 Django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间
urlpatterns = [
	url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),#视图函数2
    url(r'^$', views.IndexView.as_view(), name='index'),#视图函数1
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),#匹配年和月
	url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),#匹配目录
	url(r'^about/$',views.about,name='about'),
	url(r'^all_blogs/$',views.all_blogs,name='all_blogs'),
	url(r'^contact_me/$',views.contact_me,name='contact_me'),
	url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
	#url(r'^search/$', views.search, name='search'),
	
]