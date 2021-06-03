# -*- coding: utf-8 -*-

from sdnet.netconf import *

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
        '''
        # temp
        manufacturer = "h3c"
        drv = driver_map[manufacturer]
        ret = drv.get_switch()
        return ret