# -*- coding: utf-8 -*-

from sdnet import utils

class Cnetconf(object):
    
    def __init__(self,type):
        self.driver_type = type

    def __str__(self):
        return self.driver_type
    
    @staticmethod
    def create_vlan(self,vlan_id):
        raise NotImplementedError
    
    @staticmethod
    def create_vlanif(self,ip):
        raise NotImplementedError

def get_driver(name):
    return utils.get_driver(name)


driver_map = {
    "h3c": get_driver("h3c"),
    "hw": get_driver("hw"),
    "cisco": get_driver("cisco"),
}

__all__ = ('driver_map',)