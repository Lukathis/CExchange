from django.conf.urls import url
from django.contrib import admin
from Blog import views

urlpatterns = [
    url(r'^index$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<article_id>[0-9]+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<category_id>\d+)$', views.CategoryView.as_view(), name='category'),
url(r'^admin/', admin.site.urls, name='admin'),
]