# kek note 
# version 1.0.0

import sys, os
from datetime import datetime

version = "1.0.0"
notebook_name = "default"

class Notebook:
    def __init__(self, filename='default'):
        self.filename = filename
        self.notes = {}
        self.timestamps = {}
        self.load()
    
    ''' Lists notes from selected notebook '''
    def list_notes(self):
        for i in self.notes.iterkeys():
            print(str(i) + ' [' + str(self.timestamps[i]) + ']\t', self.notes[i])

    ''' Add a note to the selected notebook. '''
    def add_note(self, note):
        i = len(self.notes) + 1
        dt = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
        self.notes[i] = note
        self.timestamps[i] = dt.strftime('%Y%m%d%H%M%S')

        ''' Write the note to file '''
        with open(self.filename, 'a') as nb:
            nb.write(str(self.timestamps[i]))
            nb.write(" #" + str(i) + '\t')
            nb.write(note)
            nb.write('\n')
        
    def delete_note(self, note):
        # if param is note id
        if note in self.notes.keys():
            del self.notes[note]
            del self.timestamps[note]
        # if param is note timestamp
        else:
            i = list(self.notes.keys())[list(self.timestamp.values()).index(note)]
            del self.notes[i]
            del self.timestamps[i]
    
    ''' (Re)writes all notes from the dictionary to the notebook file '''
    def write_notes(self):
        with open(self.filename, 'w') as nb:
            for i, notes in self.notes.values():
                nb.write(str(self.timestamps[i]))
                nb.write(" #" + str(i) + '\t')
                nb.write(notes)
                nb.write('\n')

    ''' Loads a notebook from file '''
    def load(self):
        with open(self.filename, 'r') as nb:
            for lines in nb:
                notes = lines.rstrip().split('\t')
                notes = notes.pop(0).split(' ') + notes
                timestamp = notes[0]
                i = int(notes[1][1])
                note = notes[2]
                self.notes[i] = note
                self.timestamps[i] = timestamp 

def current_version():
    return "kek note version " + version

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

load()

if __name__ == '__main__':
    args = sys.argv
    if "--version" in args: 
        print(current_version())