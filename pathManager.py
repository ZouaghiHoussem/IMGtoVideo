import os
import glob

def is_exist(path):
    if path.find('.') == -1:
        if not os.path.isdir(path):
            print ("Error: Folder doesn't exist")
            return False
    else:
        if not os.path.isfile(path):
            print ("Error: File doesn't exist")
            return False
    return True


def get_name(path):
    start_index = path.rfind('/')
    end_index = path.rfind('_')
    if end_index < 0:
        end_index = path.rfind('.')
    return path[start_index+1:end_index]


def get_extension(path):
    end_index = path.rfind('.')
    if end_index < 0 or end_index==0:
        print ("Error: {0} is not a folder".format(path))
        return False
    return path[end_index+1:]


def get_folder(path):
    last_slash=path.rfind('/')
    return path[:last_slash+1]


def get_name_extension(path):
    start_index = path.rfind('/')
    end_index = path.rfind('_')
    if end_index < 0:
        end_index = path.rfind('.')
    return path[start_index+1:end_index], path[end_index+1:]

    '''  
    FN name : find_paths
    Summary : 
        Find one/list of paths using *, ?, 
        and character ranges expressed with [] 
    inputs  :
        path: string = The input path: Example: ./in/* or ./in/*1*.jpg
        is_sorted: bool  = is the output sorted
    '''


def find_paths(path, is_sorted=False):
    path_list = glob.glob(os.path.expanduser(path))

    if len(path_list) == 0:
        print ("Error: No path found using {0}".format(path))
        return False

    if is_sorted:
        path_list.sort(key=lambda x: get_name(x))
    return path_list


