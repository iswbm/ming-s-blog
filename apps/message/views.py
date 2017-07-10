#  coding:utf-8
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from .models import Message, Comment, MessageBoard
from article.models import Articles, Category, Tags
from sites.models import UsefulLinks, MySite
from users.models import UserProfile, VisitView

# Create your views here.


class MessageView(View):
    def get(self, request):
        #  增加访问量
        visit = VisitView.objects.all()[0]
        visit.visit_nums += 1
        visit.save()

        messages = Message.objects.all().order_by("-add_time")
        article_nums = Articles.objects.count()
        cat_nums = Category.objects.count()
        tag_nums = Tags.objects.count()
        #  博主信息
        author = UserProfile.objects.get(is_staff=True)
        #  友情链接
        links = UsefulLinks.objects.all()
        #  我的网站
        sites = MySite.objects.all()
        board = MessageBoard.objects.all()[0]
        return render(request, 'message.html', {
            'messages': messages,
            'article_nums': article_nums,
            "cat_nums": cat_nums,
            "tag_nums": tag_nums,
            "author": author,
            "links": links,
            "sites": sites,
            "board": board,
            "visit_nums": visit.visit_nums,
        })

    def post(self, request):
        if request.user.is_authenticated():
            new_message = Message()
            new_message.content = request.POST.get("message", "")
            new_message.user = request.user
            new_message.save()
            from django.core.urlresolvers import reverse
            return HttpResponseRedirect(reverse('message'))
        else:
            return render(request, 'login.html')


class CommentView(View):
    def post(self, request, article_id):
        if request.user.is_authenticated():
            article = Articles.objects.get(id=article_id)
            title = article.title
            new_comment = Comment()
            new_comment.user = request.user
            new_comment.content = request.POST.get("comment", "")
            new_comment.article = article
            new_comment.save()
            from django.core.urlresolvers import reverse
            return HttpResponseRedirect(reverse("article", kwargs={"title":title, "is_com":1}))
        else:
            return render(request, 'login.html')
