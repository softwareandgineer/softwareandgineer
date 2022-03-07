import os


def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_files(path, prefix=""):
    if prefix == "":
        print("Folder listing for", path)
        prefix = "|"

    dirlist = get_dirlist(path)
    for file in dirlist:
        print(prefix + file)
        fullname = os.path.join(path, file)
        if os.path.isdir(fullname):
            print_files(fullname, prefix + "| ")


print_files("..")
