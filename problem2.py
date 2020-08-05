import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
      if path.endswith(suffix) and suffix != '':
        return [path]
      else:
        return []

    subdirectory = os.listdir(path)
    file_list = []

    for item in subdirectory:
      if os.path.isfile(os.path.join(path,item)) == True:
        if item.endswith(suffix) and suffix != '':
          file_list.append(os.path.join(path,item))
      else:
        file_list.extend(find_files(suffix,os.path.join(path,item)))

    return file_list

if __name__ == "__main__":

  def print_return(r):
    for i in r:
      print(str(i))

  #Test1   
  print('-- Test 1 --')     

  my_path = "./Test/testdir"
  suffix = ".c"
  path_list = find_files(suffix,my_path)
  print(path_list)
  
  r1 = ['./testdir/subdir1/a.c','./testdir/subdir5/a.c', './testdir/t1.c','./testdir/subdir3/subsubdir1/b.c']
  print('Expect to see: ')
  print(r1)

  #Test2
  print('-- Test 2 --')
  my_path2 = "./Test/a"
  suffix2 = ".txt"
  path_list2 = find_files(suffix2,my_path2)
  print(path_list2)
  
  r2 = ['.Test/a/b/c/e/f/hello.txt']
  print('Expect to see: ')
  print(r2)

  #Test3 
  print('-- Test 3 --')
  my_path3 = "./Test/a"
  suffix3 = ""
  path_list3 = find_files(suffix3,my_path3)
  print(path_list3)
  
  r3 = []
  print('Expect to see: ')
  print(r3)

  #Test4
  print('-- Test 4 --')
  my_path4 = "./Test/a/b/c/e/f/hello.txt"
  suffix4 = ".txt"
  path_list4 = find_files(suffix4,my_path4)
  print(path_list4)
  
  r4 = ["./Test/a/b/c/e/f/hello.txt"]
  print('Expect to see: ')
  print(r4)

