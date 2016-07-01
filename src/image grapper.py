from os import chdir
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from os import walk
from os.path import curdir
from urllib.request import urlretrieve
from os.path import pardir
from src.create_dir import create_directory

GOOGLE_IMAGE = 'https://www.google.co.in/search?site=&tbm=isch&source=hp&biw=1920&bih=949&'


def image_grabber(ch):
    if ch == 1:
        print('Enter data to download Images: ')
        data = input()
        search_query = {'q': data}
        search = urlencode(search_query)
        print(search)
        g = GOOGLE_IMAGE+search
        request = Request(g, headers={'User-Agent': 'Mozilla/5.0'})
        r = urlopen(request).read()
        sew = BeautifulSoup(r, 'html.parser')
        count = 0
        for links in sew.find_all('img'):
            urlretrieve(links.get('src'), 'img'+str(count)+'.jpg')
            count += 1
        return True

    elif ch == 2:
        for folders, subfolder, files in walk(curdir):
            for folder in subfolder:
                print(folder)
        return True

    elif ch == 3:
        print('Enter the directory to be set: ')
        data = input()
        chdir(data + ':\\')
        print('Enter name for the folder: ')
        data = input()
        create_directory(data)
        return True

    elif ch == 4:
        print(
            '''
-------------------------***Thank You For Using***-------------------------
            '''
        )
        return False


run = True

print(
    '''
***********[First Creating Folder To Save Your Images}***********
    '''
)
create_directory('Images')
DEFAULT_DIRECTORY = pardir+'\\Images'
chdir(DEFAULT_DIRECTORY)


while run:
    print('''
-------------------------WELCOME-------------------------
    1. Search for image
    2. View Images in your directory
    3. Set directory
    4. Exit
-------------------------*******-------------------------
    ''')
    choice = input()
    run = image_grabber(int(choice))
