"""ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from test import views

urlpatterns = [
    url(r'^mail/$', views.test_mail),
    url(r'^mail_html/$', views.test_mail_html),
    url(r'^mail_attach/$', views.test_mail_with_attach),
    url(r'^mail_image/$', views.test_mail_with_image),
    url(r'^angular/$', views.angular),
    url(r'^upload/$', views.upload),
    url(r'^upload_sub/$', views.upload_sub),
]
