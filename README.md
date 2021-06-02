# ccnet
Manage Netdevice.

## 部署

1. 安装依赖:

    `yum install python3 mysql-devel python3-devel.x86_64  -y`
    
    `pip3 install django uwsgi mysqlclient requests`

    `pip3 install django-celery-results celery celery[redis] django-celery-beat`

2. 服务安装:

- 修改配置文件: ccnet/ccnet_conf.py
- 默认监听80端口
- 部署：
`# ./deploy.sh`
- 服务启动:
`# systemctl start ccnet`

## 单元测试

**运行全部测试**

`# ./manage.py test sdnet/tests`

**运行指定测试案例**

`# ./manage.py test sdnet.tests.{}`
