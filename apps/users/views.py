#  coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm, UploadForm, ResetForm
from .models import UserProfile, EmailVerifyRecord
from utils.email_send import send_register_email
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from utils.mixin_utils import LoginRequiredMixin


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    from django.core.urlresolvers import reverse
                    return HttpResponseRedirect(reverse('homepage'))
                else:
                    return render(request, 'login.html', {'msg': '用户未激活', "login_form": login_form})
            else:
                return render(request, 'login.html', {"msg": "用户名或者密码错误"})
        else:
            return render(request, 'login.html', {"login_form": login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {
            "register_form": register_form,
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)  # 运行到这一步就会验证'验证码'是否正确
        if register_form.is_valid():
            email = request.POST.get('email', "")
            username = request.POST.get('username', '')
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {"msg": "用户已注册", "register_form": register_form})
            pass_word = request.POST.get('password', "")
            user_profile = UserProfile()
            user_profile.username = username
            user_profile.email = email
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)  # 将密码进行加密
            user_profile.save()

            send_register_email(email, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class ActivateView(View):
    def get(self, request, activate_code):
        all_record = EmailVerifyRecord.objects.filter(code=activate_code)
        if all_record:
            for record in all_record:
                email = record.email
                user_profile = UserProfile.objects.get(email=email)
                user_profile.is_active = True
                user_profile.save()
                user_profile.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user_profile)
        else:
            return render(request, 'active_fail.html')
        from django.core.urlresolvers import reverse
        return HttpResponseRedirect(reverse('user:upload'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        from django.core.urlresolvers import reverse
        return HttpResponseRedirect(reverse('homepage'))


class UpLoadImageView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'active_success.html')

    def post(self, request):
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            image = request.FILES["image"]
            user = request.user
            user.image = image
            user.save()
            from django.core.urlresolvers import reverse
            return HttpResponseRedirect(reverse('homepage'))
        else:
            pass


class SendCodeView(View):
    def post(self, request):
        form = ResetForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email", "")
            is_user = UserProfile.objects.filter(email=email)
            if is_user:
                send_register_email(email, send_type="forget")
                return HttpResponse('{"status":"success","msg":"发送成功，请前往查看！"}', content_type="application/json")
            else:
                return HttpResponse('{"status":"fail","msg":"该邮箱尚未注册，请注册！"}', content_type="application/json")
        else:
            return HttpResponse('{"status":"fail","msg":"请输入正确的邮箱地址！"}', content_type="application/json")


class ResetView(View):
    def get(self, request):
        reset_form = ResetForm()
        return render(request, 'forgetpwd.html', {'reset_form': reset_form})

    def post(self, request):
        reset_form = ResetForm(request.POST)
        if reset_form.is_valid():
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            is_user = UserProfile.objects.filter(email=email)
            if is_user:
                user = is_user[0]
                user.password = make_password(password)
                user.save()
                return render(request, 'login.html')
        else:
            return render(request, 'forgetpwd.html', {'reset_form':reset_form})


#  全局404处理函数
def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


# 全局500处理函数
def page_error(request):
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
