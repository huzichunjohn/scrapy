#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('gbk')

import urllib2
from StringIO import StringIO
import gzip

request = urllib2.Request('http://www.qq.com')
request.add_header('Accept-encoding', 'gzip')
response = urllib2.urlopen(request)
print response.info().get('Content-Encoding')
if response.info().get('Content-Encoding') == 'gzip':
    buf = StringIO(response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
else:
    data = response.read()

data = data.encode('utf-8')
print data
