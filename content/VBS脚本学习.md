Title: VBS脚本学习
Date: 2021-3-28 17:00
Category: IT
Tags: Vim
Authors: leelongcrazy
Summary: windows下VBS脚本学习

# VBS脚本学习

## Demo one

``` vbscript

# 启动notepad程序
set obj = CreateObject('Wscript.Shell')
ojb.Run('notepad')
=》 
?

# ping 百度，后台静默运行
set obj = CreateObject("Wscript.Shell")
obj.Run "ping www.baidu.com",0

```

run 有三个参数:

第一个参数是你要执行的程序的路径

第二个程序是窗口的形式

​	0是在后台运行；

​	1表示正常运行

​	2表示激活程序并且显示为最小化

​	3表示激活程序并且显示为最大化

​	一共有10个这样的参数我只列出了4个最常用的。

第三个参数是表示这个脚本是等待还是继续执行，如果设为了true,脚本就会等待调用的程序退出后再向后执行。



## VBS and CMD

程序框架：

```vbscript
set objshell=createobject("wscript.shell")
objshell.run("%comspec% /k **********"),1,true

## 第一行，打开一个命令行窗口。
## %comspec% 是一个指向当前命令行外壳的环境变量。通过使用 %comspec%，您不必担心命令行外壳是 cmd.exe 还是 command.exe；%comspec% 会自动选择正确的一个。
## 在调用你给出的命令后，确保窗口始终保持打开。这就是 /k 参数的用处。如果我们想要确保命令窗口会在你给出的命令调用完成后被自动关闭，应该将 /k (keep) 修改为 /c (close)。

```

