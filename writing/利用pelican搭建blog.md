# 利用pelican搭建GitHub blog

## 安装



```bash
## 显示调试信息
pelican -v -D

## 提交到远程仓库
ghp-import -m "Generate Pelican site" -b main "绝对路径/output"
git push origin main
```

