"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from disk import views as disk_view



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^disk/', include('disk.urls', namespace="disk")),

    # url(r'^disk/', disk_view.register),
    # url(r'^login/', disk_view.login),
    # url(r'^checkcode/', disk_view.get_check_code_image),

]
