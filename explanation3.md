Design Choices:
Creating the huffman tree I used a min heap as suggested to speed up the time complexity. 

To encode the data I wrote a recursive function that searched the tree and saved the bit encoding of each unique character to a dictionary. When we converted the string to its huffman bits we can use O(1) lookup from the dictionary.

Time Complexity:
O(nlogn)
The mean heap takes O(logn) time for insertion, sorting, and popping off the next lowest values. And we have to do this n times for each value. This would be O(nlogn).

In our case N is the number of unique characters which is usually not very large (26 letters in alphabet) and this time complexity is not as important.

Space Complexity:
O(n)
The tree itself is of size n. 
