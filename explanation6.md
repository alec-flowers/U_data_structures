Design Choices:
I traverse each linked list and add each item to a set. For union I'm done and for intersection you can lookup the values against each other in O(1) time

Time Complexity:
N = size of list1
M = size of list2 
O(N+M)
Traversing the linked lists and adding the items to a set is O(N+M) time. 

Space Complexity:
N = size of list1
M = size of list2
O(N+M)
Created a set that will be worst case same size as the linked lists.  
