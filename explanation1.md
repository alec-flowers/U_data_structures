The requirement for this was O(1) time complexity. 

Design Choices:
I used a doubly linked list in conjuction with a hash table to keep every operation at O(1) time. I could have used an OrderedDict but in the spirit of everyhting we had just learned wanted to use the data structures. The doubly linked list keeps the order of the items and makes taking nodes out when we reach capacity O(1) time. The hash table allows me to tell when we get a cache "hit" in O(1) time and re-order the linked list. 

Time Complexity:
O(1)
The linked list appends and pops in O(1) time since we keep a pointer to the head and the end.
The hash table looks up items in O(1) time. 

Space Complexity:
O(N) + O(N)
We are storing items in a two data structures, a hash table and a linked list. This is not super efficient but allows us the speed we are looking for. 