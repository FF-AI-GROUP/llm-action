安装包(指定阿里云镜像)
pip install requests==2.32.3 -i https://mirrors.aliyun.com/pypi/simple

#安装jupyter
pip install jupyter -i https://mirrors.aliyun.com/pypi/simple

#启动Jupyter多文档界面：Lab支持多文档界面，用户可以同时打开和查看多个文档，包括笔记本、文本文件、终端等。
jupyter lab

#启动Jupyter单文档界面：Notebook使用单文档界面，每次只能编辑和查看一个笔记本。
jupyter notebook