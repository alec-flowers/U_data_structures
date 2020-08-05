Design Choices:
Found this to be a similar problem as problem 2. Used recursion to loop through every item. I added them to a set which then makes the loopup O(1)

Time Complexity:
N = users
O(N)
Initial recursion to add items to the set is O(N) since we have to go look and check every item.

Space Complexity:
N = users
O(N)
The set is all of the users which could potentially be N.  
