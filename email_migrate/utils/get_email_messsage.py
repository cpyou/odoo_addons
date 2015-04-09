# -*- coding: utf-8 -*-

import urllib3

server = 'http://mail.163.com/'

http = urllib3.PoolManager()

http.request('post', server, {'username': 'cpyoulv@163.com', 'password': 'haoyunqiwyyx'})

url = 'http://mail.163.com/js6/main.jsp?sid=NCSQIbwSwkFhBJvalESSJvlxFrADLQMw&df=unknow#module=mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D'
r = http.request('GET', url)

print r.status, r.data