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

## 增加pyenv管理

* 安装：

  ``` bash
    brew install pyenv
    # or 
    apt install pyenv
  ```

* 使用

``` bash
pyenv 1.2.21
Usage: pyenv <command> [<args>]

常用命令:
   --version   显示版本信息
   activate    激活虚拟环境
   commands    列出所有可用pyenv命令
   deactivate   退出虚拟环境
   exec        按选定python版本运行
   global      设置或显示全局python版本
   help        帮助信息
   hooks       List hook scripts for a given pyenv command
   init        Configure the shell environment for pyenv
   install     Install a Python version using python-build
   local       Set or show the local application-specific Python version(s)
   prefix      Display prefix for a Python version
sed: RE error: illegal byte sequence
   rehash      Rehash pyenv shims (run this after installing executables)
   root        Display the root directory where versions and shims are kept
   shell       Set or show the shell-specific Python version
   shims       List existing pyenv shims
   uninstall   Uninstall a specific Python version
   version     Show the current Python version(s) and its origin
   version-file   Detect the file that sets the current pyenv version
   version-name   Show the current Python version
   version-origin   Explain how the current Python version is set
   versions    List all Python versions available to pyenv
   virtualenv   Create a Python virtualenv using the pyenv-virtualenv plugin
   virtualenv-delete   Uninstall a specific Python virtualenv
   virtualenv-init   Configure the shell environment for pyenv-virtualenv
   virtualenv-prefix   Display real_prefix for a Python virtualenv version
   virtualenvs   List all Python virtualenvs found in `$PYENV_ROOT/versions/*`.
   whence      List all Python versions that contain the given executable
   which       Display the full path to an executable
   
   
## 示例：
# 1.创建虚拟环境
pyenv virtualenv 3.8.6 virtualenv-name
# 2. 激活虚拟环境
pyenv activate virtualenv-name
# 3. 列出所有虚拟环境
pyenv virtualenvs
# 4. 删除虚拟环境
pyenv virtualenv-delete virtualenv-name
# 5. 推出虚拟环境
pyenv deactive
```