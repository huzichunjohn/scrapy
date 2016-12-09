#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
print urllib2.urlopen(u'http://www.baidu.com/wd=你好'.encode('utf-8')).read()
