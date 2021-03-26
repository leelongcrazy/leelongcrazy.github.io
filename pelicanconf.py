#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'leelongcrazy'
SITENAME = "leelongcrazy's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = u"%y年%m月%d日"

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

STATIC_PATHS = ['images']

# THEME='pelican-bootstrap3'
THEME='/Users/leelong/Github/pelican-themes/octopress'

PLUGIN_PATHS = ['/Users/leelong/Github/pelican-plugins']
PLUGINS = ['liquid_tags',
]

# I18N_SUBSITES = {
#     'en':dict(
#         LOCALE= 'en_US.UTF-8',
#         SITENAME= "leelongcrazy's blog"
#     ),
# }
# JINJA_EXTENSIONS = ['jinja2.ext.i18n']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('LeeLongCrazy', 'http://leelongcrazy.com'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/leelongcrazy'),
          ('Twitter', 'https://twitter.com/leelongcrazy'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
