import os

def createDir(directory):
    if not os.path.exists(directory):
        print('Creating project directory' + directory)
        os.makedirs(directory)
