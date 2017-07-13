#  coding:utf-8

from django.shortcuts import render

from django.views.generic import View
from .models import Articles, Category, ArticleTag, Tags
from sites.models import UsefulLinks, MySite
from users.models import UserProfile, VisitView
from message.models import Message, Comment
from sites.models import SecWebCategory
from bs4 import BeautifulSoup
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
# Create your views here.


class HomeView(View):
    def get(self, request):
        #  增加访问量
        visit = VisitView.objects.all()[0]
        visit.visit_nums += 1
        visit.save()

        visit_nums = str(visit.visit_nums)
        articles = Articles.objects.all().order_by("-add_time")
        article_nums = articles.count()
        cat_nums = Category.objects.count()
        tag_nums = Tags.objects.count()
        #  博主信息
        author = UserProfile.objects.get(is_staff=True)
        #  友情链接
        links = UsefulLinks.objects.all()
        #  我的网站
        sites = MySite.objects.all()
        #  我的网站
        sites = MySite.objects.all()
        #  对首页文章进行分页--起始逻辑
        try:
            page = request.GET.get('page', 1)  # 第一次访问首页，没有page参数，就给默认1，点页数后，request中就有page参数传进来，就可以知道要拿取第几页的信息
        except PageNotAnInteger:
            page = 1

        P = Paginator(articles, 10, request=request)
        articles = P.page(page)
        return render(request, 'index.html', {
            "articles": articles,
            "request": request,
            "author": author,
            "article_nums": article_nums,
            "cat_nums": cat_nums,
            "tag_nums": tag_nums,
            "links": links,
            "sites": sites,
            "visit_nums": visit_nums,
        })


class CategoryView(View):
    def get(self, request):
        #  增加访问量
        visit = VisitView.objects.all()[0]
        visit.visit_nums += 1
        visit.save()

        categories = Category.objects.all()
        cat_count = categories.count()
        article_nums = Articles.objects.count()
        cat_nums = Category.objects.count()
        tag_nums = Tags.objects.count()
        #  博主信息
        author = UserProfile.objects.get(is_staff=True)
        #  友情链接
        links = UsefulLinks.objects.all()
        #  我的网站
        sites = MySite.objects.all()
        return render(request, 'category_list.html', {
            'categories': categories,
            'cat_count': cat_count,
            'article_nums': article_nums,
            "cat_nums": cat_nums,
            "tag_nums": tag_nums,
            "author": author,
            "links": links,
            "sites": sites,
            "visit_nums": visit.visit_nums,
        })


class ArchiveView(View):
    def get(self, request):
        #  增加访问量
        visit = VisitView.objects.all()[0]
        visit.visit_nums += 1
        visit.save()

        articles = Articles.objects.all().order_by('-add_time')
        article_count = articles.count()
        cat_nums = Category.objects.count()
        tag_nums = Tags.objects.count()
        #  博主信息
        author = UserProfile.objects.get(is_staff=True)
        #  友情链接
        links = UsefulLinks.objects.all()
        #  我的网站
        sites = MySite.objects.all()
        return render(request, 'archives.html', {
            'article_count': article_count,
            'articles': articles,
            "cat_nums": cat_nums,
            "tag_nums": tag_nums,
            "author": author,
            "links": links,
            "sites": sites,
            "visit_nums": visit.visit_nums,
        })


class TagView(View):
    def get(self, request):
        #  增加访问量
        visit = VisitView.objects.all()[0]
        visit.visit_nums += 1
        visit.save()

        tags = Tags.objects.all()
        count = tags.count()
        article_nums = Articles.objects.count()
        cat_nums = Category.objects.count()
        tag_nums = Tags.objects.count()
        #  博主信息
        author = UserProfile.objects.get(is_staff=True)
        #  友情链接
        links = UsefulLinks.objects.all()
        #  我的网站
        sites = MySite.objects.all()
        return render(request, 'tags.html', {
            'tags': tags,
            'count':count,
            'article_nums': article_nums,
            "cat_nums": cat_nums,
            "tag_nums": tag_nums,
            "author": author,
            "sites": sites,
            "visit_nums": visit.visit_nums,
        })


class ArticleTagView(View):
    def get(self, request, tag_name):
        #  增加访问量
        visit = VisitView.objects.all()[0]
        visit.visit_nums += 1
        visit.save()

        tag = Tags.objects.get(name=tag_name)
        articles_tag = tag.articletag_set.all()
        count = articles_tag.count()
        article_nums = Articles.objects.count()
        cat_nums = Category.objects.count()
        tag_nums = Tags.objects.count()
        #  博主信息
        author = UserProfile.objects.get(is_staff=True)
        #  友情链接
        links = UsefulLinks.objects.all()
        #  我的网站
        sites = MySite.objects.all()
        return render(request, 'tag_article.html', {
            'articles_tag': articles_tag,
            'count': count,
            'tag_name': tag_name,
            'article_nums': article_nums,
            "cat_nums": cat_nums,
            "tag_nums": tag_nums,
            "author": author,
            "sites": sites,
            "visit_nums": visit.visit_nums,
        })


class SecWebView(View):
    def get(self, request):
        #  增加访问量
        visit = VisitView.objects.all()[0]
        visit.visit_nums += 1
        visit.save()

        web_cats = SecWebCategory.objects.all()
        article_nums = Articles.objects.count()
        cat_nums = Category.objects.count()
        tag_nums = Tags.objects.count()
        #  博主信息
        author = UserProfile.objects.get(is_staff=True)
        #  友情链接
        links = UsefulLinks.objects.all()
        #  我的网站
        sites = MySite.objects.all()
        return render(request, 'SecWeb.html', {
            'web_cats': web_cats,
            'request': request,
            'article_nums': article_nums,
            "cat_nums": cat_nums,
            "tag_nums": tag_nums,
            "author": author,
            "links": links,
            "sites": sites,
            "visit_nums": visit.visit_nums,
        })


class CountView(View):
    def get(self, request):
        #  增加访问量
        visit = VisitView.objects.all()[0]
        visit.visit_nums += 1
        visit.save()

        articles = Articles.objects.all().order_by("-view_nums")[:20]
        article_nums = Articles.objects.count()
        cat_nums = Category.objects.count()
        tag_nums = Tags.objects.count()
        #  博主信息
        author = UserProfile.objects.get(is_staff=True)
        #  友情链接
        links = UsefulLinks.objects.all()
        #  我的网站
        sites = MySite.objects.all()
        return render(request, 'count.html', {
            'articles': articles,
            'article_nums': article_nums,
            "cat_nums": cat_nums,
            "tag_nums": tag_nums,
            "author": author,
            "links": links,
            "sites": sites,
            "visit_nums": visit.visit_nums,
        })


class ArticleView(View):
    def get(self, request, title, is_com):
        #  增加访问量
        visit = VisitView.objects.all()[0]
        visit.visit_nums += 1
        visit.save()

        article = Articles.objects.get(title=title)
        md = markdown.Markdown(extensions=[
                                  'markdown.extensions.extra',
                                  'markdown.extensions.codehilite',
                                  'markdown.extensions.toc',
                                  TocExtension(slugify=slugify),
                              ])
        article_md = md.convert(article.content)
        article.view_nums += 1
        article.save()
        article_nums = Articles.objects.count()
        cat_nums = Category.objects.count()
        tag_nums = Tags.objects.count()
        #  博主信息
        author = UserProfile.objects.get(is_staff=True)
        #  友情链接
        links = UsefulLinks.objects.all()
        #  我的网站
        sites = MySite.objects.all()
        #  用beautiful获取标题
        # content_html = article.content
        # soup = BeautifulSoup(content_html, "html.parser")
        # tags_in_html = soup.find_all(['h1', 'h2'])
        # tags_in_html = [unicode(tag) for tag in tags_in_html]

        #  获取评论
        comments = Comment.objects.filter(article=article)

        #  获取标签
        article_tags = ArticleTag.objects.filter(article=article)
        return render(request, 'article.html', {
            'article': article,
            # 'tags_in_html': tags_in_html,
            'article_tags': article_tags,
            'is_com': is_com,
            'comments': comments,
            'article_nums': article_nums,
            "cat_nums": cat_nums,
            "tag_nums": tag_nums,
            "author": author,
            "sites": sites,
            "links": links,
            "visit_nums": visit.visit_nums,
            "article_md": article_md,
            "toc": md.toc,
        })


class CategoryListView(View):
    def get(self, request, category):
        #  增加访问量
        visit = VisitView.objects.all()[0]
        visit.visit_nums += 1
        visit.save()

        category_obj = Category.objects.get(name=category)
        articles = Articles.objects.filter(category=category_obj)
        article_nums = Articles.objects.count()
        cat_nums = Category.objects.count()
        tag_nums = Tags.objects.count()
        #  博主信息
        author = UserProfile.objects.get(is_staff=True)
        #  友情链接
        links = UsefulLinks.objects.all()
        #  我的网站
        sites = MySite.objects.all()
        return render(request, 'category_post_list.html', {
            'articles': articles,
            'category': category,
            'article_nums': article_nums,
            "cat_nums": cat_nums,
            "tag_nums": tag_nums,
            "author": author,
            "sites": sites,
            "links": links,
            "visit_nums": visit.visit_nums,
        })
