import os
import glob

def Log(msg,debug_mode=False):
    if debug_mode:
        print(msg)

def is_exist(path,debug_mode=False):
    if path.find('.') == -1:
        if not os.path.isdir(path):
            Log("Error: Folder doesn't exist")
            return False
    else:
        if not os.path.isfile(path):
            Log("Error: File doesn't exist")
            return False
    return True


def get_name(path,debug_mode=False):
    start_index = path.rfind('/')
    end_index = path.rfind('.')
    Log("Name limits are [{0},{1}]".format(start_index,end_index), debug_mode=debug_mode)
    return path[start_index+1:end_index]



def async (path,debug_mode=False):
    end_index = path.rfind('.')
    if end_index < 0 or end_index==0:
        Log("Error: {0} is not a folder".format(path),debug_mode=debug_mode)
        return False
    return path[end_index+1:]


def get_folder(path):
    last_slash=path.rfind('/')
    return path[:last_slash+1]


'''
    FN name : get_name_extension
    Summary :
        find the name and extension of the file
    inputs  :
        path: string = File path:
    return  :
        file_name, file_extension

    '''
def get_name_extension(path):
    start_index = path.rfind('/')
    end_index = path.rfind('_')
    if end_index < 0:
        end_index = path.rfind('.')
    return path[start_index+1:end_index], path[end_index+1:]


def is_image(path):
    img_extension = ["PNG", "JPG","JPEG"]
    _,extension = get_name_extension(path)
    if(extension.upper() in img_extension):
        return True
    else:
        return  False

'''
    FN name : find_paths
    Summary :
    Find one/list of paths using *, ?,
    and character ranges expressed with []
    inputs  :
    path: string = The input path: Example: ./in/* or ./in/*1*.jpg
    is_sorted: bool  = is the output sorted
    '''


def find_paths(path, is_sorted=False,debug_mode=False):
    if (path.find('*') == -1 and path.find('?') == -1 and path.find('[') == -1):
        path += '*'

    path_list = glob.glob(os.path.expanduser(path))
    
    if len(path_list) == 0:
        Log("Error: No path found using {0}".format(path),debug_mode=debug_mode)
        return False
    
    if is_sorted:
        path_list.sort(key=lambda x: get_name(x))
    return path_list



