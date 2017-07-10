#  coding:utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.


class UsefulLinks(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"博客名字")
    link = models.URLField(verbose_name=u"链接地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"友情链接"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class MySite(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"网站名称")
    link = models.URLField(verbose_name=u"链接地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"我的网站"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class SecWebCategory(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"网站一级分类")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"网站一级分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_group_set(self):
        return self.webgroup_set.all()


class WebGroup(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"网站二级分类")
    category = models.ForeignKey(SecWebCategory, verbose_name=u"网站一级分类")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"网站二级分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_url_set(self):
        return self.weburl_set.all()


class WebUrl(models.Model):
    url = models.URLField(max_length=100, verbose_name=u"网址")
    name = models.CharField(max_length=20, verbose_name=u"网站名称")
    group = models.ForeignKey(WebGroup, verbose_name=u"网站二级分类")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"网址"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name