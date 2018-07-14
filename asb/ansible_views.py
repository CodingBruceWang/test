from django.shortcuts import render
import os
import commands
import logging
from django.http.response import HttpResponse

# Create your views here.

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir_inventory = base_path + '/asb/inventory'
dir_playbook = base_path + '/asb/playbook'

def test_vbs(request):
    logging.info('============================== vbs test ==============================')
    return HttpResponse('test')


def ansible_playbook(host_group, playbook):
    '''
    :param hosts list
    :param username
    :return: execute result
    '''

    exec_cmd = 'set -o pipfail;ansible-playbook -i %s/%s %s/%s' % (dir_inventory, host_group, dir_playbook, playbook)
    logging.info('playbook_cmd===%s' % exec_cmd)
    status, output = commands.getstatusoutput('bash -c %s' % exec_cmd)
    logging.info('status===%s, output===%s' % (status, output))
    return status, output


def adhoc_cmd():

    return ''
