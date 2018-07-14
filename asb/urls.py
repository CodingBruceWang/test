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
from asb import views

urlpatterns = [
    url(r'^test/$', views.test_vbs),
    url(r'^asb_plb/$', views.ansible_playbook),
    url(r'^celery_test/$', views.celery_test),
    url(r'^start_mis1c10/$', views.start_mis1c10),
    url(r'^stop_mis1c10/$', views.stop_mis1c10),
    # url(r'^config_no_pws/$', views.config_no_pws),
    url(r'^mail_test/$', views.mail_test_1),
]
