ICS
===

工业控制系统的用户角色管理系统

运行环境要求：python2.7，python2.7-virtualenv,django-1.6.7,django-xadmin

1.安装virtualenv，下载官方的源码包,编译，安装：
下载地址：https://pypi.python.org/pypi/virtualenv

2.进入虚拟环境下，pip install -r requirements.txt

3.同步数据库： python manage.py syncdb

4.测试：python manage.py runserver
