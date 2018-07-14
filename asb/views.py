# -*- coding: UTF-8 -*-
from django.shortcuts import render
import logging
import os
import commands
from django.http.response import HttpResponse

# Create your views here.
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_vbs(request):
    logging.info('============================== vbs test ==============================')
    return HttpResponse('test')


def ansible_playbook(request):
    '''
    :param hosts list
    :param username
    :return: execute result
    '''
    # dir_base = 'base_path===%s' % base_path
    # dir_inventory = base_path + '/asb/inventory'
    # dir_playbook = base_path + '/asb/playbook'
    # asb_web_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/startapache2.yml'%(dir_inventory, dir_playbook)
    # logging.info('asb_cmd===%s' % asb_web_cmd)
    # status_web, output_web = commands.getstatusoutput('bash -c %s'%asb_web_cmd)
    # logging.info('status===%s, output===%s' % (status_web, output_web))
    # logging.info('================================================================================================')
    # if check_result(output_web):
    #     asb_app_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/startapp.yml'%(dir_inventory, dir_playbook)
    #     logging.info('asb_app_cmd===%s' % asb_app_cmd)
    #     status_app, output_app = commands.getstatusoutput('bash -c %s' % asb_app_cmd)
    #     if check_result(output_app):
    #         asb_cm_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/start_cm.yml' % (dir_inventory, dir_playbook)
    #         logging.info('asb_cm_cmd===%s' % asb_cm_cmd)
    #         status_cm, output_cm = commands.getstatusoutput('bash -c %s' % asb_cm_cmd)
    # return HttpResponse('status===%s, output===%s' % (status_cm, output_cm))
    return ''


def celery_test(request):
    from asb.tasks import test_add
    test_add.delay(1, 2)
    return HttpResponse('testing...')


def start_mis1c10(request):
    from asb.tasks import start_mis1c10
    start_mis1c10.delay()
    # start_mis1c10()
    return HttpResponse('starting mis1c10...')


def stop_mis1c10(request):

    return ''


def mail_test_1(request):
    from asb.tasks import mail_test_2
    mail_test_2.delay()
    return HttpResponse('mail test...')
