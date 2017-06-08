#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.conf.urls import url,include
from views import *

urlpatterns = [
    url(r'^register/', register, name='register'),
    url(r'^login/', login, name='login'),
    url(r'^checkCode/', get_check_code_image, name='checkCode'),
]