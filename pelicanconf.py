#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Andrew Z Allen"
SITENAME = u"Andrew Z Allen"
SITEURL = 'http://andrewzallen.com'
SITEURL = ''
RELATIVE_URLS = True
TIMEZONE = 'America/Denver'
TWITTER_USERNAME = 'achew22'
GITHUB_URL = 'http://github.com/achew22/'
DISQUS_SITENAME = "achew22-blog"
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (1989, 7, 17, 19, 7, 22)
DEFAULT_LANG = 'en'


FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Static file list
STATIC_PATHS = [
]

# Don't generate PDFs yet
PDF_GENERATOR = False

# Typography
TYPOGRIFY = False

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

DISPLAY_PAGES_ON_MENU = False

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Files To Copy
FILES_TO_COPY = (
    ('extras/robots.txt', 'robots.txt'),
    ('extras/htpasswd', 'htpasswd'),
    ('extras/favicon.ico', 'favicon.ico')
)

# Files not to copy
IGNORE_FILES = [
    'theme/css/*.less',
    'static/css/bootstrap'
]

# Plugins
PLUGIN_PATH = 'pelican-plugins'

import sys
sys.path.insert(0, "plugins")

import preprocess_metainformation as preprocess_metainformation
import run_script as run_script
import static_generator as static_generator
import impress_js as impress_js

PLUGINS = [
    'assets',
    #'code_include',
    'multi_part',
    'html_rst_directive',

    preprocess_metainformation,
    run_script,
    static_generator,
    impress_js,
    #'pelican.plugins.related_posts',
]

# Related posts config
RELATED_POSTS = {
    'numentries': 2,
}

DELETE_OUTPUT_DIRECTORY = True

ASSET_CONFIG = (
    ('closure_compressor_optimization', 'WHITESPACE_ONLY'),
    ('less_bin', 'lessc'),
)

THEME = 'themes/andrewallen'

# Blogroll
LINKS = (
    ('My Employer', 'https://www.gospotcheck.com/'),
    ('TechStars', 'http://www.techstars.com'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'twitter', 'https://twitter.com/achew22'),
    ('GitHub', 'github', 'https://github.com/achew22'),
    ('Google Plus', 'google-plus', 'https://plus.google.com/110942846399558932785/'),
    ('Facebook', 'facebook', 'https://facebook.com/achew22'),
)

TEMPLATE_PAGES = {
    'pages/404.html' : '404.html',
    'pages/work.html': 'work/index.html',
    'pages/resume.tex': 'resume.tex',
}

# Define useful filters
def resume_format(value, format='%B %Y'):
    print type(value), value
    return value.strftime(format)

def media_url(url, site_root):
    if re.match("^https?://", "https://yahoo.com", re.IGNORECASE):
        return url
    else:
        return "%s/%s" %(site_root, url)

JINJA_EXTENSIONS = ['jinja2.ext.loopcontrols']
JINJA_FILTERSS = {
    "resume_format": resume_format,
    "media_url": media_url,
}

SUMMARY_MAX_LENGTH = 100

DEFAULT_PAGINATION = 10
