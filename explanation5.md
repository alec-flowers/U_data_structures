Design Choices:
Used a linked list to connect the blocks. The hash portion takes in all the new data as well as the hash of the last block. 

Time Complexity:
N = blocks
O(N)
Adding an item to the chain is O(1), since we just add to the front of the linked list. Doing this for every block would be O(N)

Space Complexity:
N = blocks
O(N)
The linked list will be the size of blocks that we add to it. 
