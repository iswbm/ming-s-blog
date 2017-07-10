# _*_ coding:utf-8 _*_
__author__ = 'Alon'
__date__ = '2017/7/7 17:59'

from django import forms
from captcha.fields import CaptchaField
from users.models import UserProfile


class RegisterForm(forms.ModelForm):
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})

    class Meta:
        model = UserProfile
        fields = ['email', 'username', 'nick_name', 'password']


class UploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


class ResetForm(forms.ModelForm):
    captcha = forms.CharField(error_messages={"required": u"你忘记输入验证码了喂"})

    class Meta:
        model = UserProfile
        fields = ['email', 'password']