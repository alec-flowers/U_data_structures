The requirement for this was O(1) time complexity. 

Design Choices:
I used an Ordered dict which allows me to add and delete items from the beginning an end at O(1) time since its implemented as a linked list. Since its a dict its also a hash table which allows me to check the items in the dict in O(1) time

Time Complexity:
N = cached items
O(1)
The linked list appends and pops in O(1) time since we keep a pointer to the head and the end.
The hash table looks up items in O(1) time. 

Space Complexity:
N = Cached items
O(N) + O(N)
We are storing items in a two data structures, a hash table and a linked list. This is not super efficient but allows us the speed we are looking for. 