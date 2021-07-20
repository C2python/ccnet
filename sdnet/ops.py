# -*- coding: utf-8 -*-

from sdnet.svc import l2

actions = {
    "TestTask": l2.test_task,
    "GetSwitch": l2.get_switch,
    "CreateVlan": l2.create_vlan,
    "AddSwitch": l2.add_switch,
}