Title: Git使用指南 
Date: 2019-5-28 17:00
Category: IT
Tags: Tech,Git
Authors: leelongcrazy
Summary: github常用命令解析

Git使用指南
===
看懂Git命令，搞懂版本控制
---

### Git，版本控制必备手段，程序员黑客Linus Benedict Torvalds发明了这个有名的版本控制工具，他还是Linux内核的发明人和这个计划的合作者。

### `git init`
#### 这是创建一个新的项目要做的第一件事，在项目文件目录下创建一个`.git`的存储库（隐藏文件夹），存储库（repo）是你对项目文件的修改按照时间顺序存储的集合，记录下所有更改的记录。

### `git config`
```sh
$:git config --global user.name "Your name"
$:git config --global user.email "YourEmail@xxx.com"
```
#### 用来设置你提交时候需要设置的信息，只在Git安装之后设置一次就可以了。

### `git add filename`
#### 可以添加任何你想添加的文件到暂存区（staging area）。

### `git add .`
#### 可以将项目文件夹下所有文件放到暂存区，而不用一个一个添加。

### `git status`
#### 显示所有你已经放进暂存区的文件，和进行了修改需要放进暂存区的文件。

### `git reset filename`
#### 从暂存区删除指定文件

### `git rm --cached filename`
#### 从暂存区删除指定文件，并将其设置为未跟踪。

### `git commit -m "Description of the commit"`
#### 从暂存区获取文件，并将它们提交到本地存储库。引号部分为修改文件的描述，注意一定要写的简单清晰，不可省略。

### `touch .gitignore`
#### 创建一个名叫.gitignore的文件，可以通过文本编辑的方式写下存储库需要忽略的文件名或文件夹名，运行时候这些被忽略的文件不会显示。

### `git branch branchName`
#### 创建一个代码分支，就是前一个分支代码库的直接副本。如果不加分支名字可以列出当前代码库的分支情况，前面带有`*`号的分支即为你当前所在分支。

### `git checkout "branchName"`
#### 检查你创建的分支，并在这个分支上工作，通俗的讲就是分支切换。

### `git merge branchName`
#### 这个命令把分支`branchName`合并到当前分支。

### `git remote add origin https://github.com/UserName/projectName.git`
#### 添加远程存储库的位置。在此之前的操作都是在本地完成，此步需要登录GitHub账号创建一个远程存储库，然后把本地存储库的文件放上去。创建远程存储库之后会生成一个链接，可以放在上面的命令中。

### `git remote`
#### 和项目关联的远程存储库列表。

### `git push -u origin master`
#### 将本地存储库推送到远程存储库，第一次执行命令时直接这样写就好。

### `git push`
#### 在执行完初始推送后把代码刚到GitHub上。

### `git clone https://github.com/userName/projectName.git`
#### 将项目远程仓库的代码clone到你本地计算机。

### `git clone -b branchName https://github.com/userName/projectName.git`
#### 将远程仓库`branchName`分支的代码clone到本地计算机。

### `git add -A && git commit -a -m "description" && git push --all`
#### 一行命令搞定代码提交。

### `git pull`
#### 如果你和别人用一样的代码库，这个命令可以让你从远程存储库获取最新版本，更新你的本地版本，这样就可以在别人的基础上继续写代码了。
