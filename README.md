# common
## 1.setup django
- django-admin startproject common -- 创建项目
- python manage.py startapp commonapp -- 创建应用
- pip install django pillow
- python manage.py runserver/python manage.py runserver 8080

## 2.setup mysql
- download https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.13-winx64.zip
- install: mysqld --initialize --console (root@localhost: :K.kgd%7=oKu)
- start: net start mysql
- stop: net stop mysql
- remove: mysqld --remove
- config: my.conf
    [mysqld]
    # 设置3306端口
    port=3306
    ### 设置mysql的安装目录
    basedir=D:\DevelopeSoft\Mysql\mysql-8.0.13-winx64
    ### 设置mysql数据库的数据的存放目录
    datadir=D:\DevelopeSoft\Mysql\mysql-8.0.13-winx64\data
    ### 允许最大连接数
    max_connections=200
    ### 允许连接失败的次数。
    max_connect_errors=10
    ### 服务端使用的字符集默认为UTF8
    character-set-server=utf8
    ### 创建新表时将使用的默认存储引擎
    default-storage-engine=INNODB
    ### 默认使用“mysql_native_password”插件认证
    ### mysql_native_password
    default_authentication_plugin=mysql_native_password
    [mysql]
    ### 设置mysql客户端默认字符集
    default-character-set=utf8
    [client]
    ### 设置mysql客户端连接服务端时默认使用的端口
    port=3306
    default-character-set=utf8
 
 - database: create database python;
 - user: create user 'python'@'%' identified by '2wsx@WSX';
 - delete: delete from mysql.user where user='python';
 - update: update mysql.user set authentication_string=password('Abcd1234') where user='python';
 - privileges: GRANT ALL PRIVILEGES ON python.* to python@'%' IDENTIFIED BY '2wsx@WSX' WITH GRANT OPTION;
 - grant: show grants for python;
 - flush: flush privileges; 
## 3.update databases
- python manage.py makemigrations/python manage.py makemigrations commonapp
- python manage.py sqlmigrate commonapp 0001
- python manage.py migrate
## 4.create superuser
- python manage.py createsuperuser
## 4.documents
    https://docs.djangoproject.com/zh-hans/2.1/
    