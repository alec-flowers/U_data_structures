from collections import OrderedDict

class LRU_cache(object):
        def __init__(self,capacity):
                self.capacity = capacity
                self.size = 0
                self.cache = OrderedDict()

        def get(self, key):
                'See if key is in the cache. If it is return the value otherwise return -1'

                #Change order of dict to reflect recent usage if get() is called
                if key in self.cache:
                        value = self.cache[key]
                        del self.cache[key]
                        self.cache[key] = value

                        return self.cache[key]
                else:
                        return -1

        def set(self, key, value):
                'Add key and value. If above capacity remove oldest used value' 

                if self.size >=  self.capacity:
                        self.cache.popitem(last=False)
                        self.size-=1
                self.cache[key] = value
                self.size += 1

if __name__ == "__main__":
        #Tests
        our_cache = LRU_cache(5)

        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)


        print(our_cache.get(1))       # returns 1
        print(our_cache.get(2))       # returns 2
        print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

        our_cache.set(5, 5) 
        our_cache.set(6, 6)
        our_cache.set(7,7)
        our_cache.get(7)
        our_cache.get(1)

        print(our_cache.get(3))
        print(our_cache.get(2))

