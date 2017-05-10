# CExchange
An experience share and Q&amp;A website for civil engineers.
本项目目前已经迁移到新的项目gongxinshi，可移步新项目仓库查看。

### 项目运行方式
开发环境为 python3.4，推荐使用pyenv + virtualenv搭建虚拟环境使用。

1. fork 本项目到仓库并克隆至本地
2. 迁移数据库，在 manage.py 所在目录执行

        python manage.py makemigrations
        python manage.py migrate

3. 运行命令创建超级用户
    
        python manage.py createsuperuser

7. 在 manage.py 所在目录开启本地服务

        python manage.py runserver

8. 浏览器输入 http://127.0.0.1:8000/

### 第三方包

pillow
markdown2


# Authors
Xu Chi
