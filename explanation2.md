
Design Choices:
I sovled this problem recursively because it made sense to check each folder and call the function again for any new folders that were found.

Time Complexity:
O(N)
We have to iterate through all the files and check each one of them. This means we will have to look at all O(N) items. 

Space Complexity:
O(N)
I have a list that stores the files that matches our condition. This is a structure that takes space and could take O(N-1) space if there is one folder in tons of files matching out condition.