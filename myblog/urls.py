# coding:utf-8
"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from article.views import HomeView, CategoryView, ArchiveView, TagView
from message.views import MessageView, CommentView
from article.views import SecWebView, CountView, ArticleView, CategoryListView, ArticleTagView
from users.views import SendCodeView
import xadmin
from django.views.static import serve
from myblog.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', HomeView.as_view(), name='homepage'),
    url(r'^category/$', CategoryView.as_view(), name='category'),
    url(r'^category_list/(?P<category>.+)/$', CategoryListView.as_view(), name='category_list'),
    url(r'^archives/$', ArchiveView.as_view(), name='archive'),
    url(r'^tags/list/$', TagView.as_view(), name='tag'),
    url(r'^tag/(?P<tag_name>.+)/$', ArticleTagView.as_view(), name='tag_article'),
    url(r'^messages/$', MessageView.as_view(), name='message'),
    url(r'^comments/(?P<article_id>\d+)/$', CommentView.as_view(), name='comment'),
    url(r'^SecWeb/$', SecWebView.as_view(), name='secweb'),
    url(r'^count/$', CountView.as_view(), name='count'),
    url(r'^article/(?P<title>.+)&(?P<is_com>.+)/$', ArticleView.as_view(), name='article'),

    url(r'^user/', include("users.urls", namespace='user')),

    url(r'^sendcode/$', SendCodeView.as_view(), name='sendcode'),

    # 富文本相关
    # url(r'^ueditor/', include('DjangoUeditor.urls')),
    # 验证码
    url(r'^captcha/', include('captcha.urls')),

    # 媒体文件
    url(r'^media/(?P<path>.*/)', serve, {"document_root": MEDIA_ROOT}),
]

# 配置全局404页面
handle404 = 'users.views.page_not_found'
handle500 = 'users.views.page_error'
