#!/usr/bin/env python

import os, json, cgi

print "Content-type: text/html"
print
print "<HTML><BODY><h1>Hello, World!</h1>"
print "<form method='POST'><input name='x'></form>"
print
form = cgi.FieldStorage()
print "<P>X was: " + cgi.escape(str(form.getvalue('x'))) + "</p>"


print "</BODY></HTML>"
