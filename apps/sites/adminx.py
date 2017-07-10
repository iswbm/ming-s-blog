# _*_ coding:utf-8 _*_
__author__ = 'Alon'
__date__ = '2017/7/9 14:07'

import xadmin
from .models import UsefulLinks, MySite, SecWebCategory, WebGroup, WebUrl


class UsefulLinksAdmin(object):
    list_display = ['name', 'link']


class MysiteAdmin(object):
    list_display = ['name', 'link']


class SecWebCategoryAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']


class WebGroupAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']


class WebUrlAdmin(object):
    list_display = ['url', 'group', 'add_time']
    search_fields = ['url', 'group', 'add_time']
    list_filter = ['url', 'group', 'add_time']

xadmin.site.register(UsefulLinks, UsefulLinksAdmin)
xadmin.site.register(MySite, MysiteAdmin)
xadmin.site.register(SecWebCategory, SecWebCategoryAdmin)
xadmin.site.register(WebGroup, WebGroupAdmin)
xadmin.site.register(WebUrl, WebUrlAdmin)