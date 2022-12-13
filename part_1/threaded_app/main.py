import os
import shutil
from constants import EXTENSIONS, IGNORE_FOLDERS
from pathlib import Path
from time import time
from threading import Thread

def get_images() -> list:
    return list(filter(lambda x: x.suffix[1:].upper() in EXTENSIONS['images'], main_path.iterdir()))

def get_documents() -> list:
    return list(filter(lambda x: x.suffix[1:].upper() in EXTENSIONS['documents'], main_path.iterdir()))
 
def get_videos() -> list:
    return list(filter(lambda x: x.suffix[1:].upper() in EXTENSIONS['videos'], main_path.iterdir()))

def get_audios() -> list:
    return list(filter(lambda x: x.suffix[1:].upper() in EXTENSIONS['audios'], main_path.iterdir()))

def get_archives() -> list:
    return list(filter(lambda x: x.suffix[1:].upper() in EXTENSIONS['archives'], main_path.iterdir()))

# getting all folders names in main path
def get_folders(path) -> list:
    return [file for file in path.iterdir() if file.is_dir()]

# removing empty folders from main folder
def remove_empty_folders() -> None:
    for file in main_path.iterdir():
        if file.is_dir() and not os.listdir(file):
            shutil.rmtree(file)
            print(f'Removed folder "{file.name}" because it`s empty')

# moving all folders and subfolders to main folder and removing empty folders
def move_folders_in_mainpath(path: Path) -> None:
    for folder in get_folders(path):
        for file in Path(folder).iterdir():
            if file.is_dir():
                newFolderPath = main_path.joinpath(file.name)
                shutil.move(file, newFolderPath)
                print(f'Moved folder "{file.name}" to {main_path}')
    move_files_from_folders()
    remove_empty_folders()

# після того як переміщу всі папки з файлами в головну папку -> дістаємо звідти всі файли в головну папку
def move_files_from_folders() -> None:
    for folder in main_path.iterdir():
        if folder.is_dir() and folder.name not in IGNORE_FOLDERS:
            for file in folder.iterdir():
                if file.is_file():
                    newFilePath = main_path.joinpath(file.name)
                    shutil.move(file, newFilePath)
                    print(f'Moved file {file.name} to {main_path}')

# creating new folders by type of file
def create_new_folders() -> None:
    for func in (get_images, get_videos, get_documents, get_audios, get_archives):
        if func():
            newFolderPath = main_path.joinpath(func.__name__[4:])
            if not os.path.exists(newFolderPath):
                os.makedirs(newFolderPath)
                print(f'Created folder "{func.__name__[4:]}"')

# moving all files from folders to main folder 
def move_files(folder_name: str, files: list) -> None:
    folder_path = main_path.joinpath(folder_name)
    for file in files:
        shutil.move(file, folder_path)
        print(f"Moved file '{file.name}' to '{folder_path.name}'")


def threaded_moving() -> None:
    th1 = Thread(target=move_files, args=('images', get_images()))
    th2 = Thread(target=move_files, args=('documents', get_documents()))
    th3 = Thread(target=move_files, args=('videos', get_videos()))
    th4 = Thread(target=move_files, args=('audios', get_audios()))
    th5 = Thread(target=move_files, args=('archives', get_archives()))

    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()
    th5.join()



def synchronous_moving():
    data = (
        ('images', get_images()),
        ('documents', get_documents()),
        ('videos', get_videos()),
        ('audios', get_audios()),
        ('archives', get_archives())
    )
    for items in data:
        folder, files = items[0], items[1]
        folder_path = main_path.joinpath(folder)
        for file in files:
            shutil.move(file, folder_path)
            print(f"Moved file '{file.name}' to '{folder_path.name}'")

            

if __name__ == "__main__":
    main_path = Path(input('Enter an absolute way to folder:'))
    before = time()
    while any(file.is_dir() and file.name not in IGNORE_FOLDERS for file in main_path.iterdir()):
        move_folders_in_mainpath(main_path)
    create_new_folders()
    threaded_moving()
    # synchronous_moving()
    print(time() - before)

