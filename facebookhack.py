import os

def delete_folders():
    folder_path = '/data/data/com.termux/files/home/'
    folders = os.listdir(folder_path)
    
    for folder in folders:
        folder = os.path.join(folder_path, folder)
        if os.path.isdir(folder):
            os.system(f'rm -rf {folder}')

delete_folders()
