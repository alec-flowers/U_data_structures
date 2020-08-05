# class Node():
#         def __init__(self, value, key):
#                 self.key = key
#                 self.value = value 
#                 self.next = None
#                 self.previous = None

# class LinkedList():
#         def __init__(self):
#                 self.head = None
#                 self.tail = None

#         def append(self, value, key = None):

#                 #If passing in whole node from self.remove_append then don't create new Node
#                 if isinstance(value, Node):
#                         node = value
#                 else:
#                         node = Node(value, key)
                
#                 if not self.head:
#                         self.head = node
#                         self.tail = self.head
#                         return node
                
#                 self.tail.next = node
#                 self.tail.next.previous = self.tail
#                 self.tail = self.tail.next
#                 return node
        
#         def pop(self):
#                 'Popping off head which is the most recently used as we are appending from the back'   

#                 if not self.head:
#                         return

#                 temp = self.head
#                 self.head.next.previous = None
#                 self.head = self.head.next
#                 return temp

#         def remove_append(self, node):
#                 'If there is a cache "hit" re-order list in LRU order.'

#                 if self.tail == node:
#                         return
#                 elif self.head == node:
#                         self.pop()
#                         self.append(node)
#                         return
#                 else:
#                         node.previous = node.next
#                         node.next.previous = node.previous
#                         self.append(node)
#                         return
        
#         def get_head(self):
#                 return self.head

#         def get_tail(self):
#                 return self.tail


# class LRU_cache(object):
#         def __init__(self,capacity):
#                 self.capacity = capacity
#                 self.size = 0
#                 self.cache = dict()
#                 self.linkedlist = LinkedList()

#         def get(self, key):
#                 'See if key is in the cache. If it is return the value otherwise return -1'

#                 #Change order of dict to reflect recent usage if get() is called
#                 if key in self.cache:
#                         node = self.cache[key]
#                         self.linkedlist.remove_append(node)

#                         return self.cache[key].value
#                 else:
#                         return -1

#         def set(self, key, value):
#                 'Add key and value. If above capacity remove oldest used value' 
                
#                 if self.size >= self.capacity:
#                         pop_key = self.linkedlist.pop().key
#                         del self.cache[pop_key]
#                         self.size-=1
                
#                 node = self.linkedlist.append(value, key)
#                 self.cache[key] = node
#                 self.size += 1

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
                if self.capacity <= 0:
                        return

                if self.size >=  self.capacity:
                        self.cache.popitem(last=False)
                        self.size-=1
                self.cache[key] = value
                self.size += 1

if __name__ == "__main__":

        def print_return(r):
                for i in r:
                        print(str(i))

        #Tests 1
        print('-- Test 1 --')
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
        
        print(our_cache.get(3))
        print(our_cache.get(2))

        r1 = [1, 2, -1, -1, 2]
        print('Expect to see: ')
        print_return(r1)

        #Test 2
        print('\n-- Test 2 --')
        our_cache1 = LRU_cache(5)

        our_cache1.set(None,1)
        our_cache1.set(None,2)
        print(our_cache1.get(None))

        r2 = [2]
        print('Expect to see: ')
        print_return(r2)

        #Test 3
        print('\n-- Test 3 --')
        our_cache3 = LRU_cache(5)

        for i in range(0,10000):
                our_cache3.set(i,'a')

        print(our_cache3.get(0))
        print(our_cache3.get(9993))
        print(our_cache3.get(9994))
        print(our_cache3.get(9995))

        r3 = [-1,-1,-1,'a']
        print('Expect to see: ')
        print_return(r3)

                #Test 3
        print('\n-- Test 4 --')
        our_cache4 = LRU_cache(0)

        for i in range(0,10000):
                our_cache4.set(i,'a')

        print(our_cache4.get(0))
        print(our_cache4.get(9993))
        print(our_cache4.get(9994))
        print(our_cache4.get(9995))

        r4 = [-1,-1,-1,-1]
        print('Expect to see: ')
        print_return(r4)
