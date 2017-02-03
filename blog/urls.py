from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^article/(\d+)/', views.viewArticle, name = 'article'),
    url(r'^$', views.post_list),
]