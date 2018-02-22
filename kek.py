# kek note 
# version 1.0.0

import sys, os
from datetime import datetime
from notebook import Notebook

version = "1.0.0"
notebook_name = "default"

load()

def current_version():
    return version

''' Loads variables from settings file '''
def load():
    with open('settings.txt', 'r') as f:
        version = f.readline().rstrip().split(' ')[-1]
        notebook_name = f.readline().rstrip().split(' ')[-1]

''' Updates settings file '''
def config():
    with open('settings.txt', 'r') as f:
        f.write("version = " + str(version))
        f.write("\nnotebook_name = " + notebook_name)

# Notebook commands 
''' Shows current notebook being used. '''
def current_nb():
    print(notebook_name)

''' Lists down all existing notebooks. '''
def list_all():
    for files in os.listdir('notebooks/'):
        print(files)

''' Selects a notebook. '''
def select(notebook):
    notebook_name = notebook
    config()

''' Deletes a notebook. '''
def delete_nb(notebook):
    try:
        os.remove('notebooks/' + notebook)
    except:
        print("An error occured.")