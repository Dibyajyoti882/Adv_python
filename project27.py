#Design and implement a data structure for Least Recently Used (LRU) cache. It should support get and put operations in O(1) time
cache = []
size = 3

def use(x):
    if x in cache:
        cache.remove(x)
    elif len(cache) >= size:
        cache.pop(0)
    cache.append(x)

use(1)
use(2)
use(3)
use(1)
use(4)

print(cache)