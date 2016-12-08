"""
Code to search for the folders whose size is
Zero bytes
"""

from os.path import getsize
from os import walk
from os.path import abspath
from os.path import join
from os import chdir


def file_searcher(direct):
    chdir(direct)
    for foldername, subfolder, filename in walk(direct):
    	for subs in subfolder:
	        for file in filename:
	            if getsize(abspath(join(foldername, file))) == 0:
	                print(abspath(join(foldername, file)))


file_searcher('D:\\')