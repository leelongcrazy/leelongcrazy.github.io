Title: 在Mac上安装python虚拟环境管理工具
Date: 2020-5-29 17:00
Category: IT
Tags: Python,Code
Authors: leelongcrazy
Slug: Install-virtualenv-on-Mac
Summary: 在Mac上安装python虚拟环境管理工具

在Mac上安装python虚拟环境管理工具
---

#### 在Mac上安装完homebrew以后，测试下工具就安装python3，安装完以后发现和系统中的一些工具默认以python2执行的冲突了，执行命令的时候会报出多行错误信息，害得我一度认为我把Mac系统给玩坏了，后来重新安装了一遍python2 的pip工具，问题解决了。

[避免以后安装的库文件和Mac系统环境的依赖库重叠，最好的办法莫过于多创建虚拟环境。](https://www.cnblogs.com/kaid/p/8227635.html "在Mac上搭建Python虚拟环境")

### 安装virtualenv

##### 安装执行：
```zsh
$ pip3 install virtualenv
```
##### 创建虚拟环境，激活，退出：
```
$ virtualenv test_env
$ cd test_env  # 进入虚拟环境目录
$ source bin/activate # 激活虚拟环境
$ deactivate  # 退出虚拟环境
```

### 安装virtualenvwrapper

##### Virtaulenvwrapper是virtualenv的扩展包，可以更方便地新增，删除，复制，切换虚拟环境。

```
# 安装
$ pip3 install virtualenvwrapper
# 创建一个隐藏文件夹用以存放虚拟环境
$ mkdir .virtualenvs
# 记住下面两个命令显示的路径
$ which virtualenvwrapper.sh
$ which python3
# 编辑zsh配置文件
$ vi .zshrc
```
##### 在末尾添加下面的内容
```
export WORKON_HOME="~/.virtualenvs"
export VIRTUALENVWRAPPER_PYTHON="/usr/local/bin/python3"
source /usr/local/bin/virtualenvwrapper.sh
```
```
# 刷新shell
$ source .zshrc
```

##### virtualenvwrapper常用命令
```
# 1.list the virtualenv environments
$ lsvirtualenv -b

# 2.change virtualenv
$ workon virtualenv-name

# 3.list the installed packages
# lssitepackages

# 4.enter the current virtualenv's path
$ cdvirtualenv

# 5.enter the current virtualenv's site-packages/
$ cdsitepackages

# 6.copy virtualenv
$ cpvirtualenv env1 env2
Copying env1 as env2...

# 7.exit the virtualenv
$ deactivate

# 8.delete the virtualenv
$ rmvirtualenv virtualenv-name
```

