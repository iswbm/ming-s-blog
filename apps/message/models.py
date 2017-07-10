#  coding:utf-8
from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile
from article.models import Articles
from datetime import datetime
# Create your models here.


class Message(models.Model):
    content = models.CharField(max_length=500, verbose_name=u"留言内容")
    user = models.ForeignKey(UserProfile, verbose_name=u"留言者")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"留言板"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user.username


class Comment(models.Model):
    content = models.CharField(max_length=500, verbose_name=u"文章评论")
    article = models.ForeignKey(Articles, verbose_name=u"文章")
    user = models.ForeignKey(UserProfile, verbose_name=u"评论者")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"评论"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user.username


class MessageBoard(models.Model):
    quote = models.CharField(max_length=100, verbose_name=u"顶部引用")
    illustration = models.TextField(verbose_name=u"说明")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"留言板相关"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.quote