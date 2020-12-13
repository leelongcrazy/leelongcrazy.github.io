Title: VIM注释代码与反注释
Date: 2018-2-28 17:00
Category: IT
Tags: Vim,Code
Authors: leelongcrazy
Summary: VIM注释代码与反注释

## VIM注释代码与反注释

### 方法一： 块选择模式注释
1. 按键“V”进入 *visual模式*，选中需要注释的代码行；
2. `Ctrl + V`  进去 *块选择模式*；
3. `I`进入插入模式，输入注释符号 “#” 或者 “//”...；
4. 立即按下`ESC`键两次，即可注释完成

* 取消注释
    - `Ctrl + V`  进去 *块选择模式*；
    - 选择要删除的注释符号，按`d`删除即可

### 方法二：
* 批量注释
    - `：开始行号，结束行号/s/^/注释符号/g`
* 取消注释
    - `：开始行号，结束行号/s/^注释符号//g`


[参考链接：https://blog.csdn.net/xiajun07061225/article/details/8488210]（https://blog.csdn.net/xiajun07061225/article/details/8488210）