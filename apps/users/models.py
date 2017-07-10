#  coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("male", u'男'), ("female", u'女')), default='female')
    address = models.CharField(max_length=11, verbose_name=u'地址', null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default=u"image/default.png", max_length=100)
    phone = models.CharField(max_length=11, verbose_name=u"手机号码", null=True, blank=True)
    # image依赖Pillow

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class VisitView(models.Model):
    visit_nums = models.IntegerField(default=0, verbose_name=u"网站浏览量")
    visitor_nums = models.IntegerField(default=0, verbose_name=u"网站访客数")

    class Meta:
        verbose_name = u"浏览访客数"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.visit_nums


class VisitInfoView(models.Model):
    ip = models.CharField(max_length=20, verbose_name=u"访客IP")
    visit_time = models.DateTimeField(default=datetime.now, verbose_name=u"最近访问时间")
    visit_nums = models.IntegerField(default=0, verbose_name=u"访问次数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"首次访问时间")

    class Meta:
        verbose_name = u"访客信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.ip


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(max_length=20, choices=(("register", u'注册'), ("forget", u'找回密码'), ("update_email", u'修改邮箱')), verbose_name=u"验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")  # datetime不加括号，就生成实例时运行，加上括号，程序一运行就生成

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

