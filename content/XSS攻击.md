Title: XSS攻击
Date: 2021-3-14 18:00
Category: Web
Tags: WebSec,PWN
Authors: leelongcrazy
Summary: XSS攻击实战

# XSS攻击

### 反射型XSS

请求代码出现在URL中，作为输入提交到服务器，服务器解析后响应，响应内容中出现这段XSS代码，最后在浏览器解析执行，达到攻击效果。

``` js 
// 常用攻击payload
' onclick=alert(1)//
'"></script><script>alert(1)</script>//
```

### 存储型XSS



### DOM型XSS



