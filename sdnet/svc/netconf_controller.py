# -*- coding: utf-8 -*-

from sdnet.exceptions.ccnet_exceptions import *
from sdnet.netconf import *
from sdnet.models import Switchs

import logging

logger = logging.getLogger(__name__)

class CNetconfController(object):
    def __init__(self):
        pass
    
    def get_switch(self,params):
        logger.info("Get switch: %s" % params)
        dev_name = params["dev"]
        logger.info("Load %s drivers" % dev_name)
        '''
        Get dev manufacturer
        
        if "manufacturer" in params.keys():
            manufacturer = params["manufacturer"]
        else:
            manufacturer = "h3c"
        drv = driver_map[manufacturer]
        ret = drv.get_switch(params)
        '''
        try:
            sw = Switchs.objects.get(dev=params["dev"])
            ret = {
                "code": 0,
                "messgae": "success",
                "data":{
                    "dev": sw.dev,
                    "manufacturer": sw.manufacturer,
                    "mgmt_ip": sw.mgmt_ip,
                    "vtep_ip": sw.vtep_ip,
                    "create_at": sw.create_at,
                }
            }
        except KeyError:
            raise CcnetInvalidRequestException(INVALID_PARA)
        return ret
    
    def add_switch(self,params):
        logger.info("Add switch: %s" % params)
        # save db
        try:
            
            sws = Switchs.objects.filter(mgmt_ip=params["mgmt_ip"],deleted_at=None)
            if sws.count() > 0:
                ret = { "code": DUPLICATE_SW, "message": error_code[DUPLICATE_SW]}
                return ret
            sw = Switchs(dev=params["dev"],manufacturer=params["manufacturer"],mgmt_ip=params["mgmt_ip"],
                    vtep_ip=params.get("vtep_ip",""))
            sw.save()
        except KeyError:
            raise CcnetInvalidRequestException(INVALID_PARA)
        ret = {"code": 0, "message": "Success."}
        return ret
