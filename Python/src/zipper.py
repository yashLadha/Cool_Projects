from src.create_dir import move_folder
from zipfile import ZipFile
from os.path import abspath
from os.path import basename
from os.path import join
from os import walk
from os.path import pardir


def back_zip(folder):
    folder = abspath(folder)
    backup_zip = ZipFile('Backup_' + basename(folder)+'.zip', 'w')
    for foldername, subfolders, filenames in walk(folder):
        backup_zip.write(foldername)
        for subs in subfolders:
            for filename in filenames:
                newBase = 'Backup_'+basename(folder)
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue
                backup_zip.write(join(foldername, filename))
    backup_zip.close()
    move_folder(pardir+'\\'+'src'+'\\'+'Backup_' + basename(folder)+'.zip', 'D', 'Backup')


back_zip(pardir)
