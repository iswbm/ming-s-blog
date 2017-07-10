#  coding:utf-8
__author__ = 'Alon'
__date__ = '2017/7/4 16:23'

import xadmin
from xadmin import views
from .models import Articles, Tags, Category, ArticleTag


class GlobalSettings(object):
    site_title = u"我的博客 - 后台"
    site_footer = u"我的博客"
    menu_style = "accordion"


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class ArticlesAdmin(object):
    list_display = ['title', 'category', 'author', 'add_time']
    search_fields = ['title', 'content']
    list_filter = ['category', 'add_time']
    style_fields = {"content": "ueditor"}


class TagsAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']


class CategoryAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']


class ArticleTagAdmin(object):
    list_display = ['article', 'tag', 'add_time']
    search_fields = ['article', 'tag', 'add_time']
    list_filter = ['article__title', 'tag__name', 'add_time']


xadmin.site.register(Articles, ArticlesAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tags, TagsAdmin)
xadmin.site.register(ArticleTag, ArticleTagAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
