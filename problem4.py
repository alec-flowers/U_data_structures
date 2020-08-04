class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self):
        s = ''
        s += 'Group Name: {} \n'.format(self.name)
        for user in self.users:
            s+= ' - ' + user + '\n'
        for group in self.get_groups():
            s += '\n{}SubGroup Name: {} \n'.format('  ',group.get_name())
            for user in group.get_users():
                s += '  - '+ user + '\n'

        return s

#recursive solution to loop through groups and add users to set
#check if user matches person in set

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = set()

    def group_recursion(group):
        'Recursively iterate through groups and add users to a set'

        users.update(group.get_users())

        if not group.get_groups():
            return
        else:
            for g in group.get_groups():
                users.update(g.get_users())
                next_group = group_recursion(g)
        return next_group

    group_recursion(group)

    if user in users:
        return True
    return False

if __name__ == "__main__":

    #Test1   
    print('-- Test 1 --') 

    parent = Group("parent")
    child = Group("child")
    child2 = Group("child2")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    parent_user = 'parent_user mark'
    parent.add_user(parent_user)

    child2_user = 'child2_user alex'
    child2.add_user(child2_user)

    child.add_group(sub_child)
    parent.add_group(child)
    parent.add_group(child2)


    print(is_user_in_group('child2_user alex', parent))
    print('The value should be: \nTrue')
    #Test2
    print('-- Test 2 --')
    print(is_user_in_group('', parent))
    print('The value should be: \nFalse')
    #Test3 
    print('-- Test 3 --')
    print(is_user_in_group('a', parent))
    print('The value should be: \nFalse')