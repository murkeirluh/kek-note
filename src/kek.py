# kek note 
# version 1.0.0

import sys, os
from datetime import datetime

class Notebook:
    def __init__(self, filename='default'):
        self.filename = filename
        self.notes = {}
        self.timestamps = {}
        self.load()

    def __str__(self): return self.filename
    def __repr__(self): return self.filename
    
    ''' Lists notes from selected notebook '''
    def list_notes(self):
        
        if len(self.notes.keys()):
            for i in self.notes.keys():
                print(str(i) + ' [' + str(self.timestamps[i]) + ']\t', self.notes[i])
        else:
            print("No notes yet.")

    ''' Add a note to the selected notebook. '''
    def add_note(self, note):
        i = len(self.notes) + 1
        while (i in self.notes.keys()) or ((len(self.notes.keys())) and (i < sorted(self.notes.keys())[-1])):
            i = i + 1
        dt = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
        self.notes[i] = note
        self.timestamps[i] = dt.strftime('%Y%m%d%H%M%S')

        ''' Write the note to file '''
        with open("notebooks/" + self.filename, 'a') as nb:
            nb.write(str(i) + " [")
            nb.write(str(self.timestamps[i]))
            nb.write("]\t")
            nb.write(note)
            nb.write('\n')
        
        print("Note successfully added.")
        
    def delete_note(self, note):
        try:
            # if param is note id
            if int(note) in self.notes.keys():
                del self.notes[int(note)]
                del self.timestamps[int(note)]
                self.write_notes()
                print("Note successfully deleted.")
            # if param is note timestamp
            elif note in list(self.timestamps.values()):
                i = list(self.notes.keys())[list(self.timestamps.values()).index(note)]
                del self.notes[i]
                del self.timestamps[i]
                self.write_notes()
                print("Note successfully deleted.")
            else:
                print("Error: note doesn't exist.")
        except:
            print("An error occured.")
    
    ''' (Re)writes all notes from the dictionary to the notebook file '''
    def write_notes(self):
        with open("notebooks/" + self.filename, 'w') as nb:
            for i, notes in self.notes.items():
                nb.write(str(i) + " [")
                nb.write(str(self.timestamps[i]))
                nb.write("]\t")
                nb.write(notes)
                nb.write('\n')

    ''' Loads a notebook from file '''
    def load(self):
        try:
            with open("notebooks/" + self.filename, 'r') as nb:
                for lines in nb:
                    notes = lines.rstrip().split('\t')
                    notes = notes.pop(0).split(' ') + notes
                    timestamp = notes[1][1:-1]
                    i = int(notes[0])
                    note = notes[2]
                    self.notes[i] = note
                    self.timestamps[i] = timestamp
            sorted(self.notes)
            sorted(self.timestamps)
        except:
            # notebook does not exist yet
            with open("notebooks/" + self.filename, 'x'):
                pass

''' Loads variables from settings file '''
def load():
    global version, notebook_name, nb
    with open('settings.txt', 'r') as f:
        version = f.readline().rstrip().split(' ')[-1]
        notebook_name = f.readline().rstrip().split(' ')[-1]
    nb = Notebook(notebook_name)

''' Updates settings file '''
def config():
    global version, notebook_name
    with open('settings.txt', 'w') as f:
        f.write("version = ")
        f.write(version)
        f.write("\nnotebook_name = " + notebook_name)

### Notebook commands 

''' Lists down all existing notebooks. '''
def list_all():
    files = os.listdir('notebooks/')
    if len(files):
        for f in files:
            print('-', f)
    else:
        print("No notebooks yet.")

''' Selects a notebook. '''
def select(notebook):
    global notebook_name
    if notebook_name != notebook:
        notebook_name = notebook
        config()
        load()
        print("Notebook \'" + notebook_name + "\' selected.")
    else:
        print("Notebook \'" + notebook_name + "\' already selected.")

''' Deletes a notebook. '''
def delete_nb(notebook):
    global notebook_name
    try:
        os.remove('notebooks/' + notebook)
    except FileNotFoundError:
        print("Error: notebook does not exist.")
    except:
        print("An unknown error occured.")
    else:
        if notebook_name == notebook:
            notebook_name = "default"
            config()
        print("Notebook \'" + notebook + "\' deleted.")

global version, notebook_name, nb
version = "1.0.0"
notebook_name = "default"
nb = Notebook()

if __name__ == '__main__':
    args = sys.argv
    command = ' '.join(args)
    param = args[-1]
    load()

    if command == "kek --version" or command == "kek": 
        print("kek note", version)
    elif command == "kek notebook":
        print("Current notebook:", notebook_name)
    elif command == "kek notebook list":
        list_all()
    elif ' '.join(args[:3]) == "kek notebook select":
        select(param)
    elif ' '.join(args[:3]) == "kek notebook remove":
        delete_nb(param)
    elif command == "kek list":
        nb.list_notes()
    elif ' '.join(args[:2]) == "kek add":
        nb.add_note(param)
    elif ' '.join(args[:2]) == "kek remove":
        nb.delete_note(param)
    else:
        print("Error: Command not found.")

        