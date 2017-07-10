# _*_ coding:utf-8 _*_
__author__ = 'Alon'
__date__ = '2017/7/6 12:41'

import xadmin
from xadmin.plugins.auth import UserAdmin
from .models import VisitView, VisitInfoView

class UserProfileAdmin(UserAdmin):
    pass


class VisitViewAdmin(object):
    list_display = ['visit_nums', 'visitor_nums']
    list_filter = ['visit_nums', 'visitor_nums']


class VisitInfoViewAdmin(object):
    list_display = ['ip', 'visit_nums', 'visit_time', 'add_time']
    list_filter = ['visit_time', 'add_time']

xadmin.site.register(VisitView, VisitViewAdmin)
xadmin.site.register(VisitInfoView, VisitInfoViewAdmin)
