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
    subdirectory = os.listdir(path)
    file_list = []

    for item in subdirectory:
      if os.path.isfile(os.path.join(path,item)) == True:
        if item.endswith(suffix):
          file_list.append(os.path.join(path,item))
      else:
        file_list.extend(find_files(suffix,os.path.join(path,item)))

    return file_list

if __name__ == "__main__":
    my_path = "./testdir"
    suffix = ".c"

    path_list = find_files(suffix,my_path)
    print(path_list)
