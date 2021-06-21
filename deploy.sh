#!/bin/bash
#set -o errexit
#set -x

echo "Start Deploy CCnet..."

# 关闭服务
systemctl stop ccnet || true
systemctl stop ccnet_celery || true

user="ccnet"
group="ccnet"

#create group if not exists
egrep "^$group" /etc/group >& /dev/null
if [ $? -ne 0 ]
then
    groupadd $group
fi

#create user if not exists
egrep "^$user" /etc/passwd >& /dev/null
if [ $? -ne 0 ]
then
    useradd -g $group $user
fi

# 项目存放目录
deploy_dir="/opt/production"
project="ccnet"
if [ ! -d "$deploy_dir" ]; then
    echo "Mkdir deploy directory $deploy_dir ..."
    mkdir "$deploy_dir"
fi
# 判断项目目录是否存在
if [ ! -d "${deploy_dir}/${project}" ]; then
    echo "Mkdir project directory ${deploy_dir}/${project} ..."
    mkdir "${deploy_dir}/${project}"
else
    echo "Backup Old Project..."
    tar -cPf "${deploy_dir}/${project}-$(date +%Y-%m-%d-%H-%M).tar" "${deploy_dir}/${project}"
    rm -rf "/tmp/${project}"
    mv -f "${deploy_dir}/${project}" "/tmp/"
fi

mkdir -p /var/run/ccnet

# 部署
cur_dir=`pwd`
cp -ar ${cur_dir}/../${project} ${deploy_dir}/

# 部署systemd服务
cp -af "${cur_dir}/ccnet.service" /etc/systemd/system/
cp -af "${cur_dir}/ccnet_celery.service" /etc/systemd/system/


chown -R ccnet.ccnet /var/run/ccnet
chown -R ccnet.ccnet /var/log/ccnet
chown -R ccnet.ccnet /opt/production

# -*- 初始化动作 -*-

# 初始化数据库
pushd "${deploy_dir}/${project}"
python3 manage.py migrate
if [ $? -ne 0 ]; then
    echo "Database init failed!!!"
    exit -1
fi
popd

# 加载服务
systemctl daemon-reload 

if [ $? -ne 0 ]; then
    echo "Reload updns server failed!!!"
    exit -1
fi

echo "Deploy CCNet End."
exit 0
