# -*- coding: utf-8 -*_
# Create your tasks here

from celery import shared_task
from sdnet.models import Switchs


@shared_task
def add(x, y):
    return x + y