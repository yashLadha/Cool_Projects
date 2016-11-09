"""
Code to Search your Preferred drive for
files that are larger than 100 MB
Saerches for my D:\ drive
"""

from os.path import getsize
from os import walk
from os.path import abspath
from os.path import join
from os import chdir


def file_searcher(direct):
    chdir(direct)
    for foldername, subfolder, filename in walk(direct):
        for file in filename:
            if getsize(abspath(join(foldername, file)))/100 > 1000000:
                print(abspath(join(foldername, file)))


file_searcher('D:\\')
