# -*- coding: UTF-8 -*-
from django.shortcuts import render
import logging
import os
import commands
from django.http.response import HttpResponse

from tools.mail_tool import MailTool

def test_mail(request):
    mail_tool = MailTool()
    # mail_tool.send_mail('wangfoqing25@163.com', 'wangfoqing25@163.com', 'testing', 'smtp.163.com', '725wdmxksl163')
    mail_tool.send_mail('wangfoqing25@163.com', 'wangfoqing25@163.com', 'test mail sent...', 'mail content...')
    return HttpResponse('testing...')


def test_mail_html(request):
    mail_tool = MailTool()
    mail_tool.send_html_mail('wangfoqing25@163.com', 'wangfoqing25@163.com', 'test mail html...', 'mail html test content...')
    return HttpResponse('testing...')


def test_mail_with_attach(request):
    mail_tool = MailTool()
    mail_tool.send_mail_with_attach('wangfoqing25@163.com', 'wangfoqing25@163.com', 'test mail with attach...', 'mail with attach test content...')
    return HttpResponse('testing...')


def test_mail_with_image(request):
    mail_tool = MailTool()
    mail_tool.send_mail_with_image('wangfoqing25@163.com', 'wangfoqing25@163.com', 'test mail with image...', 'mail with image test content...')
    return HttpResponse('testing...')


def angular(request):
    print("Bubble Sort: ")
    myList = [1, 4, 5, 0, 6]
    bubbleSort(myList)
    # return render(request, "html/angular_test.html")
    return render(request, "html/test.html")


def bubbleSort(myList):
    length = len(myList)
    for i in range(0, length - 1):
        for j in range(0, length - 1 - i):
            if myList[j] > myList[j + 1]:
                tmp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = tmp
        for item in myList:
            print(item)
            print("=============================")


def upload(request):

    return render(request, 'html/file_upload.html')


def upload_sub(request):
    files = request.FILES['file1']
    file_name = files.name
    upload_dir = '/home/wfq/test/upload/'
    upload_file = upload_dir + file_name
    with open(upload_file, 'wb+') as destination:
        for chunk in files.chunks():
            destination.write(chunk)
    return render(request, 'html/file_upload.html')


