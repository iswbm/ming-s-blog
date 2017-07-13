#  coding:utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# from DjangoUeditor.models import UEditorField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"文章分类")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_article_count(self):
        return self.articles_set.count()


class Articles(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"文章标题")
    content = models.TextField(verbose_name=u"文章内容")
    abstract = models.CharField(default='', max_length=200, verbose_name=u"摘要")
    author = models.CharField(max_length=20, verbose_name=u"作者")
    category = models.ForeignKey(Category, verbose_name=u"分类")
    quote = models.CharField(max_length=100, verbose_name=u"引用", default='')
    quote_inner = models.CharField(max_length=100, verbose_name=u"文章内部引用", default='')
    view_nums = models.IntegerField(default=0, verbose_name=u"浏览人数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"最近更新时间")

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def created_year(self):
        return self.add_time.strftime("%Y")

    def created_date(self):
        return self.add_time.strftime("%m-%d")

    def created_date_all(self):
        return self.add_time.strftime("%Y-%m-%d")

    def __unicode__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=15, verbose_name=u"标签")
    nums = models.IntegerField(default=0, verbose_name=u"标签数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class ArticleTag(models.Model):
    article = models.ForeignKey(Articles, verbose_name=u"文章")
    tag = models.ForeignKey(Tags, verbose_name=u"标签")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"文章-标签"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.article.title



