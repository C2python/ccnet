from django.db import models

# Create your models here.

class Switchs(models.Model):
    dev = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=12)
    mgmt_ip = models.CharField(max_length=136)
    vtep_ip = models.CharField(max_length=136)
    create_at = models.DateTimeField("添加时间",auto_now_add=True)
    deleted_at = models.DateTimeField("删除时间",null=True, default=None)