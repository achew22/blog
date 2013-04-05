#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://andrewzallen.com'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
# Only gzip when publishing
PLUGINS += ['pelican.plugins.gzip_cache']

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

DISQUS_SITENAME = "andrewzallensblog"
GOOGLE_ANALYTICS = "UA-36726122-1"