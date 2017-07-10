# _*_ coding:utf-8 _*_
__author__ = 'Alon'
__date__ = '2017/7/8 22:29'

import xadmin
from .models import Message, Comment, MessageBoard


class MessageAdmin(object):
    list_display = ['user', 'content', 'add_time']


class CommentAdmin(object):
    list_display = ['article', 'user', 'content', 'add_time']


class MessageBoardAdmin(object):
    pass

xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(MessageBoard, MessageBoardAdmin)
