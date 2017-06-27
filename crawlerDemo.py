#coding= utf-8

import re
from collections import deque
import makeOpenner
import dealFile

queue = deque()
visited = set()

url = 'http://python.jobbole.com/77825/'

queue.append(url)
cnt = 0

while queue:

    url = queue.popleft()
    visited = {url}

    print('已经抓取：'+str(cnt)+'   正在抓取 <--' +url+ ' -->')
    cnt += 1
    oper = makeOpenner.makeMyOpener()
    uop = oper.open('http://www.baidu.com/', timeout=1000)

    if 'html' not in uop.getheader('Content-Type'):
        continue

    try:
        data = uop.read().decode('utf-8')
        dealFile.saveFile(data)
    except:
        continue

    print(data)
    dealFile.saveFile(data)
    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('Insert into queue  '  + x)




