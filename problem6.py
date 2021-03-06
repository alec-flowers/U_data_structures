class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    u = set()
    u_list = LinkedList()

    node1 = llist_1.head
    node2 = llist_2.head
    while node1:
        u.add(node1.value)
        node1 = node1.next

    while node2:
        u.add(node2.value)
        node2 = node2.next
    
    [u_list.append(val) for val in u]
    
    return u_list
    

def intersection(llist_1, llist_2):
    # Your Solution Here
    u = set()
    u1 = set()
    u2 = set()
    u_list = LinkedList()

    node1 = llist_1.head
    node2 = llist_2.head
    while node1:
        u1.add(node1.value)
        node1 = node1.next

    while node2:
        u2.add(node2.value)
        node2 = node2.next

    u = [val for val in u1 if val in u2]
    
    for val in u:
        u_list.append(val)
    
    return u_list

if __name__ == "__main__":

    #Test1   
    print('-- Test 1 --') 

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print ('Union: {}'.format(union(linked_list_1,linked_list_2)))
    print ('Intersection: {}'.format(intersection(linked_list_1,linked_list_2)))

    #Test2
    print('\n-- Test 2 --')

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print ('Union : {}'.format(union(linked_list_3,linked_list_4)))
    print ('Intersection: '.format(intersection(linked_list_3,linked_list_4)))
    print('Expectation')

    #Test3 
    print('\n-- Test 3 --')
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print ('Union : {}'.format(union(linked_list_5,linked_list_6)))
    print ('Intersection: '.format(intersection(linked_list_5,linked_list_6)))

    #Test4
    print('\n-- Test 4 --')
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = [1,2,3]
    element_2 = []

    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)

    print ('Union : {}'.format(union(linked_list_7,linked_list_8)))
    print ('Intersection: '.format(intersection(linked_list_7,linked_list_8)))