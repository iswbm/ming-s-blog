# _*_ coding:utf-8 _*_
__author__ = 'Alon'
__date__ = '2017/7/10 10:22'

from django.conf.urls import url
from .views import LoginView, RegisterView, ActivateView, LogoutView, UpLoadImageView, ResetView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^reset/', ResetView.as_view(), name='reset'),
    url(r'^upload/$', UpLoadImageView.as_view(), name="upload"),
    # 激活
    url(r'^activate/(?P<activate_code>.*)/$', ActivateView.as_view(), name='activate'),
]
