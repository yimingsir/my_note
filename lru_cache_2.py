#coding: utf-8

import collections

# version 1
class LRUCache(object):
    """ LRUCache """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

if __name__ == '__main__':
    lc = LRUCache(5)
    lc.set('zhao', 'zhaoyiming')
    lc.set('zhang', 'zhangxiaohong')
    lc.set('qian', 'qianxueshen')
    lc.set('sun', 'sunbao')
    lc.set('li', 'lixiaolu')
    lc.set('zhou', 'zhouwang')

    print lc.get('zhao')
    print lc.get('zhang')
    print lc.get('li')
