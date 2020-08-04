Design Choices:
Used a linked list to connect the blocks. The hash portion takes in all the new data as well as the hash of the last block. 

Time Complexity:
O(1)
Appending to the list is O(1).

Space Complexity:
O(N)
The linked list will be the size of blocks that we add to it. 
