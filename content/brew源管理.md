Title: brew源管理
Date: 2020-7-16 17:00
Category: IT
Tags: Tech, os
Authors: leelongcrazy
Summary: brew源管理配置

brew源管理
---
### Mac系统下brew工具源管理
1. 显示brew安装位置
``` bash
brew --repo
```
2. 查看brew目前所使用的源
``` bash
git -C "$(brew --repo)" remote get-url origin
git -C "$(brew --repo) homebrew/core" remote get-url origin
git -C "$(brew --repo) homebrew/cask)" remote get-url origin
```
3. 更换为清华源
``` bash
git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
git -C "$(brew --repo) homebrew/core" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git
brew update # 执行更新
```
4. 恢复默认源
``` bash
git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew.git
git -C "$(brew --repo homebrew/core)" remote set-url origin https://github.com/Homebrew/homebrew-core.git
git -C "$(brew --repo homebrew/cask)" remote set-url origin https://github.com/Homebrew/homebrew-cask.git
brew update # 执行更新
```
