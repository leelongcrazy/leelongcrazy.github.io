#!/bin/bash

cp CNAME ./output
ghp-import -m "Generate Pelican site" -b main "/Users/leelong/Github/leelongcrazy.github.io/output"
git push origin main
