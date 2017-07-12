#coding= utf-8

import re
from collections import deque
import makeOpenner
import dealFile
import gzip


queue = deque()
visited = set()

url = 'https://www.zhihu.com'


queue.append(url)
cnt = 0

while queue:

    url = queue.popleft()
    visited = {url}

    print('已经抓取：'+str(cnt)+'   正在抓取 <--' +url+ ' -->')
    cnt += 1
    oper = makeOpenner.makeMyOpener()
    try:
        uop = oper.open(url, timeout=1000)
        print(url)
    except:
        continue
    print(uop.getheader('Content-Type'))

    if 'html' not in uop.getheader('Content-Type'):
        continue

    try:
        data = uop.read().decode('utf-8')
        print(data)
        dealFile.saveFile(data)
    except:
        continue

    print(data)
    dealFile.saveFile(data)
    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('Insert into queue  '+ x)




#参考文章：http://python.jobbole.com/77825/