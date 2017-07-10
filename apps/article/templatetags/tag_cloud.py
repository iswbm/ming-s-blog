from __future__ import division

__author__ = 'Alon'
__date__ = '2017/7/8 23:12'


from django import template
from article.models import Tags


register = template.Library()


@register.filter
def get_font_size(value):
    top_nums = Tags.objects.all().order_by("-nums")[0].nums
    proportion = value/top_nums*20
    font_size = proportion+20
    return font_size


@register.filter
def get_transparency_1(value):
    top_nums = Tags.objects.all().order_by("-nums")[0].nums
    proportion = value / top_nums * 100
    proportion = round(proportion, 2)
    return proportion


@register.filter
def get_transparency_2(value):
    top_nums = Tags.objects.all().order_by("-nums")[0].nums
    proportion = value / top_nums
    proportion = round(proportion, 2)
    return proportion
