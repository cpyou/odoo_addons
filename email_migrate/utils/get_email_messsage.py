# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import requests

server = 'http://mail.163.com/'

r = requests.get(server, auth=('cpyoulv@163.com', 'haoyunqiwyyx'))
r.encoding = 'utf-8'
f = open('./test.html', 'w')
f.write(r.text)
# f.seek(0)
f.close()

print r.status_code