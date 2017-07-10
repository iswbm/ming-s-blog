# _*_ coding:utf-8 _*_
__author__ = 'Alon'
__date__ = '2017/7/5 11:29'

from django import template
from bs4 import BeautifulSoup

register = template.Library()


@register.filter
def get_tag_name(value):
    '''
    获取标签名
    '''
    soup = BeautifulSoup(value, 'html.parser')
    h1 = soup.h1
    h2 = soup.h2
    if h1:
        return h1.name
    elif h2:
        return h2.name
    else:
        return None


@register.filter
def get_tag_text(value):
    '''
    获取标签文本
    '''
    soup = BeautifulSoup(value, 'html.parser')
    h1 = soup.h1
    h2 = soup.h2
    if h1:
        return h1.text
    elif h2:
        return h2.text
    else:
        return None
