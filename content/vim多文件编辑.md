Title: vim多文件编辑
Date: 2021-3-28 17:00
Category: IT
Tags: Vim
Authors: leelongcrazy
Summary: 有需求利用vim同时对多个文件进行编辑的方法

# vim多文件编辑

#### 有需求利用vim同时对多个文件进行编辑的方法：
* 方法一 **在未打开文件编辑的情况下**
```
vi file1 file2 file3  # 不分屏编辑文档
vi -o file1 file2 file3 # 水平分屏编辑文档
vi -O file1 file2 file3 # 垂直分屏编辑文档

# 输入 :n 命令可转到下一文档编辑
# 输入 :N 命令可转到前一个文档编辑
# ctrl + W + W 可以实现在打开的文档之间切换
```

* 方法二 **在已经打开编辑文档，想打开第二个文档编辑的情况下：**
```
:sp file1   # 水平分屏编辑文档
:sv file1   # 水平分屏编辑文档(只读方式)
```


### 窗口分屏浏览目录
```
# 已经打开文件状态下
:He  # 在下面分屏浏览文件目录
:He! # 在上面分屏浏览文件目录
:Ve  # 左分屏浏览目录
:Ve! # 右分屏浏览目录
```

### 分屏同步移动
```
# 同步移动的两个屏中都输入如下命令
:set scb
# 解锁
:set scb!
# set scb 是 set scrollbind 的简写
```

[参考文档](https://justcode.ikeepstudying.com/2018/03/linux-vi-vim%E5%A4%9A%E6%A0%87%E7%AD%BE%E5%92%8C%E5%A4%9A%E7%AA%97%E5%8F%A3-tab%E9%A1%B5%E6%B5%8F%E8%A7%88%E7%9B%AE%E5%BD%95-%E5%A4%9Atab%E9%A1%B5%E7%BC%96%E8%BE%91/)