# -*- coding: utf-8 -*-


from sdnet import netconf
import logging

logger = logging.getLogger(__name__)

def create_vlan(**kwargs):
    '''
    kwargs:
        vlan_id: 200, vlan号
        type: 'hw', 交换机型号
        dev: {name}, 交换机名称
    options:
        vlanif_enable: bool, 是否创建vlanif
        ip: 1.1.1.1, vlanif的地址
        vpn_instance: mgmt, vrf名称
    '''
    drv = netconf.driver_map[kwargs["type"]]
    drv.connect()
    logger.debug("Create Vlan Interface")
    drv.close()
    