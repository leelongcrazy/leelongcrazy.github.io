Title: Python一行代码建立HTTP服务
Date: 2019-6-17 17:00
Category: IT
Tags: Code,Python
Authors: leelongcrazy
Summary: 在Python语言中有一条可在本机快速建立http服务的命令，可实现与他人分享存在你电脑的上的文件

#### 在Python语言中有一条可在本机快速建立http服务的命令，可实现与他人分享存在你电脑的上的文件。
```bash
python -m SimpleHTTPServer
# 默认开启8000端口，后面可跟数字指定端口
Serving HTTP on 0.0.0.0 port 8000 ...
```
#### 浏览器打开，IP：Port即可实现该目录下的浏览，文件下载。

---

#### 今天配置`.ssh/config`文件时候还犯了一个可笑的错误。在config文件中配置管理密钥的格式如下：
```bash
Hostname github.com
User git
IdentityFile ~/.ssh/github

Host aliyun
Hostname xx.xx.xx.xx
User xxx
IdentityFile ~/.ssh/aliyun

Host linux
Hostname localhost
Port 9999
User root
IdentityFile ~/.ssh/linux
```
#### 我将`IdentityFile`错误的打成了`IdentifyFile`，结果一直爆下面的错误：
```bash
.ssh/config: line 40: Bad configuration option: identifyfile
.ssh/config: terminating, 1 bad configuration options
```
#### 在网上搜索了好多结果，最终看到一文章提示有可能将单词打错导致的，才得以修正过来。原来`identity`是 *身份*的意思， `identify`是 *鉴定，辨认*的意思。配置中需要的是 `身份文件`，而不是我理解的`鉴定文件`。
