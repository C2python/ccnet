# -*- coding: utf-8 -*-


from sdnet.exceptions.ccnet_exceptions import CcnetInvalidRequestException
from sdnet.svc.netconf_controller import CNetconfController
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.http.response import HttpResponseServerError

import logging
import json

logger = logging.getLogger(__name__)

def create_vlan(request,params):
    '''
    kwargs:
        vlan_id: 200, vlan号
        type: 'hw', 交换机型号
        dev: {name}, 交换机名称
    options:
        vlanif_enable: bool, 是否创建vlanif
        ip: 1.1.1.1, vlanif的地址
        vpn_instance: mgmt, vrf名称
    Response:
    {
        "code": num;
        "message": {}
        "request_id": {}
    }
    '''

    nfc = CNetconfController()
    try:
        ret = nfc.create_vlan(params)
    except:
        return HttpResponseServerError()
    return HttpResponse(json.dumps(ret,ensure_ascii=False),content_type="application/json;charset=utf-8")
    
def get_switch(request,params):
    '''
    kwargs:
        dev: {name}, 交换机名称
    Response:
    {
        "code": num;
        "message": {}
        "request_id": {}
        "data":{

        }
    }
    '''
    nfc = CNetconfController()
    try:
        ret = nfc.get_switch(params)
    except:
        return HttpResponseServerError()
    return HttpResponse(json.dumps(ret,ensure_ascii=False),content_type="application/json;charset=utf-8")

def add_switch(request,params):
    '''
    params:
    {
        "dev": {name}, #交换机名称
        "manufacturer": "h3c", #支持h3c,hw
        "mgmt_ip": "192.168.10.1", #管理IP
        "vtep_ip": "10.10.10.5", # vtep ip可选
    }
    Response:
    {
        "code": num;
        "message": {}
        "request_id": {}
    }
    '''
    nfc = CNetconfController()
    try:
        ret = nfc.add_switch(params)
    except CcnetInvalidRequestException as err:
        err = { "code": err.code, "message": err.message}
        return HttpResponseBadRequest(json.dumps(err,ensure_ascii=False),content_type="application/json;charset=utf-8")
    except:
        return HttpResponseServerError()
    return HttpResponse(json.dumps(ret,ensure_ascii=False),content_type="application/json;charset=utf-8")