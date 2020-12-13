Title: 在Mac上安装python虚拟环境管理工具
Date: 2020-8-29 17:00
Category: IT
Tags: Bash,zsh
Authors: leelongcrazy
Summary: 如果熟悉Linux系统，一定要打交道的就是SHELL语言，掌握使用SHELL的高效方法，做起很多事情来得心应手，最开始我只熟悉bash，当我安装完zsh,并使用oh my zsh套件以后，太震撼了。

## 如果熟悉Linux系统，一定要打交道的就是SHELL语言，掌握使用SHELL的高效方法，做起很多事情来得心应手，最开始我只熟悉bash，当我安装完zsh,并使用oh my zsh套件以后，太震撼了。

### 前些天拿出吃了很久灰的树莓派，借这次安装zsh的机会，整理出来了安装的过程。

1. 查看当前使用SHELL，和已经安装的shell
```bash
echo $SHELL # 查看当前使用SHELL
➜ cat /etc/shells  # 列出已经安装的shell
/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/bin/dash
/usr/bin/dash
/usr/bin/tmux
/usr/bin/screen
/bin/zsh
/usr/bin/zsh
```
2. 如果没有显示`/bin/zsh`，则执行下面安装命令
```bash
# 我在Debian环境下安装的
sudo apt-get install zsh
# os x 下安装
brew install zsh
```
3. 安装完成后切换SHELL
```bash
sudo chsh -s /bin/zsh
```
4. 重启操作系统生效
5. 可再次查看当前SHELL`echo $SHELL`
6. 安装oh my zsh 有两种方式：`curl`和`wget`，[官方安装指导](https://github.com/ohmyzsh/ohmyzsh)
```bash
# use curl
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# or use wget
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
7.安装完成后可编辑`.zshrc`进行自定义设置，另外注意，原来`.bashrc`下的配置在`zsh`下仍然可以使用，`zsh`是完全兼容`bash`的。
