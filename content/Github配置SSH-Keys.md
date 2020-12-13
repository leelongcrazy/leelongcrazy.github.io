Title: GitHub配置SSH 
Date: 2019-5-30 17:00 
Category: IT
Tags: Tech,Git 
Authors: leelongcrazy
Summary: 对github账号配置ssh密钥对实现远程推送

GitHub配置SSH
---
---
###在使用GitHub配置ssh的时候吃了好多苦头，整理了下完整的操作过程
#### 必备工具，操作是在Linux系统环境下完成的
* Bash
* Git
* GitHub账号

#### 在使用Git工具之前需要对`git config`进行配置
```
$ git config --global user.email "xxx@xxx.com"
$ git config --global user.name "user-name"
```

#### 在`~/.ssh/`目录下创建一对公私密钥
```
$ ssh-keygen
```
#### 执行完后会在当前目录下生成两个新的文件，将后缀名.pub的公约内容复制到Github个人账号-> settings -> SSH and GPG Kyes -> New SSH key文本框中，点击` Add SSH key`添加密钥；并对添加的公钥命个别名。

#### 在终端执行下面命令：
```
$ eval `ssh-agent -s` #注意是反单引号
$ ssh-add 私钥文件名
```

#### 测试：
```
$ ssh -T git@github.com 
```
#### 测试成功显示：
```
$ Hi user-name! You've successfully authenticated, but GitHub does not provide shell access.
```
#### 接着push代码，发现仍需要输入用户名和密码，执行下面的命令， **注意连接域名和用户名之间的符号是 `:`,而不是 `/`**，删除远程仓库重新建立连接
```
$ git remote rm origin
$ git remote add origin git@github.com:user-name/repository-name.git 
```
#### 接下来远程推送的时候不再需要输入的用户名和密码。
