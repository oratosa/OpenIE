import os,glob

def path_list(directory_path:str) -> list:
    if os.path.isdir(directory_path) == True:
        directory_path = directory_path + '/**'
        path_list = glob.glob(directory_path, recursive=True)
        file_list = []
        dir_list = []
        for path in path_list:
            if os.path.isfile(path) == True:
                file_list.append(path)
            else:
                dir_list.append(path)
        return file_list, dir_list
    else:
        print("{} is not a directory path.".format(directory_path))
