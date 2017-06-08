#!/usr/bin/env python
#coding:utf-8
import md5

import datetime
import time

import cStringIO
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from models import User

from Helper import Checkcode
import StringIO
import random
# import Image, ImageDraw, ImageFont, random
from PIL import Image,ImageDraw, ImageFont   # 需要安装PIL 模块


# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    headImg = forms.FileField()


def register(request):
    if request.method == 'POST':
        print "request.POST:", request.POST
        print "request.FILES:", request.FILES
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            print "uf:", uf
            user = User()
            print "user:", user
            user.username = uf.cleaned_data['username']
            user.headImg = uf.cleaned_data['headImg']
            user.save()
            return HttpResponse('UPLOAD OK !')
    else:
        uf = UserForm()
        print "request.method:", request.method
    return render(request, 'register.html', {'uf':uf})


def checkCode(request):
    mstream = StringIO.StringIO()
    validate_code = Checkcode.create_validate_code()
    img = validate_code[0]
    img.save(mstream, "GIF")

    # 将验证码保存到session
    request.session["CheckCode"] = validate_code[1]
    return HttpResponse(mstream.getvalue())


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        check_code = request.POST.get('checkcode')
        # 从session中获取验证码
        session_code = request.session["CheckCode"]
        if check_code.strip().lower() != session_code.lower():
            return HttpResponse('验证码不匹配')
        else:
            return HttpResponse('验证码正确')

    return render_to_response('login.html', {'error': "", 'username': '', 'pwd': ''})


# def get_check_code_image(request,image='media/images/checkcode.gif'):
def get_check_code_image(request, image='c:/temp/checkcode.gif'):
    im = Image.open(image)
    draw = ImageDraw.Draw(im)
    mp = md5.new()
    mp_src = mp.update(str(time.time()))
    mp_src = mp.hexdigest()
    rand_str = mp_src[0:4]
    draw.text((10,10), rand_str[0], font=ImageFont.truetype("ARIAL.TTF", random.randrange(25,50)))
    draw.text((48,10), rand_str[1], font=ImageFont.truetype("ARIAL.TTF", random.randrange(25,50)))
    draw.text((85,10), rand_str[2], font=ImageFont.truetype("ARIAL.TTF", random.randrange(25,50)))
    draw.text((120,10), rand_str[3], font=ImageFont.truetype("ARIAL.TTF", random.randrange(25,50)))
    del draw
    # request.session['CheckCode'] = str(rand_str)
    buf = cStringIO.StringIO()
    im.save(buf, 'gif')
    return HttpResponse(buf.getvalue(), 'image/gif')
