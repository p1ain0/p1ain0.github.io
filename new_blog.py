import sys
from datetime import datetime


def get_now_time():
    """
    获取当前时间
    :return:
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


temp = '''---
title: {artical_name}
author: p1ain0
date: {now_time} +0800
categories: []
tags: []
pin: true
math: true
mermaid: true
---
'''


if __name__ == '__main__':
    artical_name = sys.argv[1]
    now_time = get_now_time()
    file_name = "./_posts/" + now_time.split(' ')[0] + '-' + artical_name + ".md"
    f = open(file_name, "w+")
    contant = temp.format(artical_name=artical_name, now_time=now_time)
    f.write(contant)
    f.close()
