# ccnet
Manage Netdevice.

## 部署

1. 安装依赖:

    `yum install python3 mysql-devel python3-devel.x86_64  -y`
    
    `pip3 install django uwsgi mysqlclient requests redis`

    `pip3 install django-celery-results celery celery[redis] django-celery-beat`

2. 服务安装:

- 修改配置文件: ccnet/ccnet_conf.py
- 默认监听80端口
- 部署：
`# ./deploy.sh`

- 服务启动,ccnet服务:
`# systemctl start ccnet`  
`# systemctl enable ccnet`

- 服务启动，celery服务
`# systemctl start ccnet_celery`  
`# systemctl enable ccnet_celery`

3. 本地调试：
- 运行ccnet
`# python3 manage.py runserver 8000`
- 运行celery
`# celery -A ccnet worker -l INFO`

## 单元测试

**运行全部测试**

`# ./manage.py test sdnet/tests`

**运行指定测试案例**

`# ./manage.py test sdnet.tests.{}`

## rabbitmq作为broker
```
# rabbitmqctl add_user ccnet passw0rd123!
# rabbitmqctl add_vhost ccnet
# rabbitmqctl set_user_tags ccnet ccnet_tag
# rabbitmqctl set_permissions -p ccnet ccnet ".*" ".*" ".*"
```