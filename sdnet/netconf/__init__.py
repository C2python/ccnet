# -*- coding: utf-8 -*-

from sdnet import utils
from . import h3c,hw

class CNetconf(object):
    
    def __init__(self,type):
        self.driver_type = type

    def __str__(self):
        return self.driver_type
    
    @staticmethod
    def create_vlan(self,**kwargs):
        raise NotImplementedError
    
    @staticmethod
    def create_vlanif(self,**kwargs):
        raise NotImplementedError

def get_driver(name):
    drv_map = {
        "h3c": h3c.H3CAgent(),
        "hw": hw.HWAgent(),
    }
    return drv_map[name]

driver_map = {
    "h3c": get_driver("h3c"),
    "hw": get_driver("hw"),
   # "cisco": get_driver("cisco"),
}

__all__ = ('driver_map',)