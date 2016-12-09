#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('GBK')

import urllib2
import gzip
import cStringIO
import time

response = urllib2.urlopen("http://www.sohu.com")
print response.info().get('Content-Encoding')
data = response.read()
data = data.encode('UTF-8')
print data
time.sleep(5)

request = urllib2.Request('http://www.sohu.com')
request.add_header('Accept-Encoding', 'gzip, deflate')
response = urllib2.urlopen(request, timeout=30)
print response.info().get('Content-Encoding')
data = response.read()

if data[:6] == '\x1f\x8b\x08\x00\x00\x00':
    data = gzip.GzipFile(fileobj=cStringIO.StringIO(data)).read()
data = data.encode('UTF-8')
print data
