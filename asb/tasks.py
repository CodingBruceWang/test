# -*- coding: utf-8 -*-
import time
from celery import Celery
from celery import task
import commands
import os
import logging
from django.http.response import HttpResponse
from tools.mail_tool import MailTool
from asb.ansible_views import ansible_playbook


# Create your views here.
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@task
def test_add(x, y):
    time.sleep(10)
    print '===================' + str(x + y)
    return x + y


def check_result(output):
    msg_success = 'unreachable=0    failed=0'
    # result = "0" if msg_success in output else result = "-1"
    if msg_success in output:
        return True
    else:
        logging.error('*******************************ansible-playbook execute failed*******************************')
        return False


def test():
    dir_base = 'base_path===%s' % base_path
    dir_inventory = base_path + '/asb/inventory'
    dir_playbook = base_path + '/asb/playbook'
    asb_web_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/startapache2.yml' % (dir_inventory, dir_playbook)
    logging.info('asb_cmd===%s' % asb_web_cmd)
    status_web, output_web = commands.getstatusoutput('bash -c %s' % asb_web_cmd)
    logging.info('status===%s, output===%s' % (status_web, output_web))
    logging.info('================================================================================================')
    if check_result(output_web):
        asb_app_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/startapp.yml' % (dir_inventory, dir_playbook)
        logging.info('asb_app_cmd===%s' % asb_app_cmd)
        status_app, output_app = commands.getstatusoutput('bash -c %s' % asb_app_cmd)
        if check_result(output_app):
            asb_cm_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/start_cm.yml' % (dir_inventory, dir_playbook)
            logging.info('asb_cm_cmd===%s' % asb_cm_cmd)
            status_cm, output_cm = commands.getstatusoutput('bash -c %s' % asb_cm_cmd)
    return HttpResponse('status===%s, output===%s' % (status_cm, output_cm))


@task
def start_mis1c10():
    logging.info('=================================enter start_mis1c10=================================')
    # dir_inventory = base_path + '/asb/inventory'
    # dir_playbook = base_path + '/asb/playbook'
    # 1. start web
    # asb_web_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/startapache2.yml' % (dir_inventory, dir_playbook)
    # status_web, output_web = commands.getstatusoutput('bash -c %s' % asb_web_cmd)
    status_web, output_web = ansible_playbook('hosts', 'startapache2.yml')
    # 2. start app
    mail_tool = MailTool()
    if check_result(output_web):
        # mail info related users
        logging.info('two web servers have been started')
        mail_tool = MailTool()
        mail_tool.send_mail('wangfoqing25@163.com', 'wangfoqing25@163.com', 'The two MIS1C10 WEB Service have been started.', 'mail content...')
        # asb_app_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/startapp.yml' % (dir_inventory, dir_playbook)
        # status_app, output_app = commands.getstatusoutput('bash -c %s' % asb_app_cmd)
        status_app, output_app = ansible_playbook('hosts', 'startapp.yml')
    # 3. start cm
        if check_result(output_app):
            logging.info('10 app servers have been started')
            mail_tool.send_mail('wangfoqing25@163.com', 'wangfoqing25@163.com', 'The ten MIST1C10 APP Service have been started.', 'mail content...')
            # asb_cm_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/start_cm.yml' % (dir_inventory, dir_playbook)
            # status_cm, output_cm = commands.getstatusoutput('bash -c %s' % asb_cm_cmd)
            status_cm, output_cm = ansible_playbook('hosts', 'start_cm.yml')
            if check_result(output_cm):
                logging.info('2 cm servers have been started, the mis1c10 cluster service has recovery.')
                mail_tool.send_mail('wangfoqing25@163.com', 'wangfoqing25@163.com', 'The two MIS1C10 CM Servers have been started. mis1c10 cluster service has been started.', 'mail content...')
            else:
                logging.error('*****************ansible-playbook execute start_cm.yml fail, please check.*****************')
                # mail info users
        else:
            logging.error('*****************ansible-playbook execute startapp.yml fail, please check.*****************')
            # mail info users
    else:
        logging.error('*****************ansible-playbook execute startapache2.yml fail, please check.*****************')
        # mail info users
    logging.info('=================================out start_mis1c10=================================')
    return ''


@task
def mail_test_2():
    logging.info('test*********************test')
    mail_tool = MailTool()
    # mail_tool.send_mail('wangfoqing25@163.com', 'wangfoqing25@163.com', 'testing', 'smtp.163.com', '725wdmxksl163')
    mail_tool.send_mail('wangfoqing25@163.com', 'wangfoqing25@163.com', 'test mail sent...kk', 'mail content')
    return HttpResponse('testing...')


def stop_mis1c10():

    return ''