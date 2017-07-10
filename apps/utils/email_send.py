# _*_ coding:utf-8 _*_
__author__ = 'Alon'
__date__ = '2017/7/7 18:18'


from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from myblog.settings import EMAIL_FROM
import random


def send_register_email(email, send_type='register'):
    email_verify_record = EmailVerifyRecord()
    if send_type == 'update_email' or send_type == 'forget':
        code = random_str(4)
    else:
        code = random_str(16)
    email_verify_record.code = code
    email_verify_record.email = email
    email_verify_record.send_type = send_type
    email_verify_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = u"MING's 个人博客 注册账号激活链接"
        email_body = u'请点击下方链接进行账号激活：http:127.0.0.1:8000/activate/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = u"MING's 个人博客 密码重置验证码"
        email_body = u'您好，你的邮箱验证码为{0}。如非本人操作，请忽略！！'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'update_email':
        email_title = u"MING's 个人博客 修改邮箱验证码"
        email_body = u'您好，你的邮箱验证码为{0}。如非本人操作，请忽略！！'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass



def random_str(randomlength=10):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

