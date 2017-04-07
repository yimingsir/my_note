#coding: utf-8

# Least Recently Used 最近最少使用算法
# version 1
class LRUCache(object):
    """ LRUCache """
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1

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
