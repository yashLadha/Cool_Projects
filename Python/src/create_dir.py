from shutil import copytree
from shutil import move
from os import chdir
from os.path import exists
from os.path import pardir
from os import makedirs
from os import removedirs
from os import rename


# Creates a directory
def create_directory(name):
    if exists(pardir+"\\"+name):
        print('Folder already exists... Cannot Overwrite this')
    else:
        makedirs(pardir+"\\"+name)


# Deletes a directory
def delete_directory(name):
    removedirs(name)


# Rename a directory
def rename_directory(direct, name):
    rename(direct, name)


# Sets the working directory
def set_working_directory():
    chdir(pardir)


# Backup the folder tree
def backup_files(name_dir, folder):
    copytree(pardir, name_dir + ':\\' + folder)


# Move folder to specific location
# Overwrites the file if it already exists
def move_folder(filename, name_dir, folder):
    if not exists(name_dir+":\\"+folder):
        makedirs(name_dir+':\\'+folder)
    move(filename, name_dir+":\\"+folder+'\\')


"""
For test purpose:
    1. create_directory("test")
    2. rename_directory("test","demo")
    3. delete_directory("demo")
    4. backup_files('D', 'backup_project')
    5. move_folder(pardir+'\\'+'test.txt', 'D', 'name')
"""
