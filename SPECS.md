# KEK NOTE SPECIFICATION
_Draft Version 0.0.1_

## Project Description:

__Project name:__ kek note
__Project description:__ a command line note taking app
__Main file:__ kek.py


## Features

_Version 1.0.0_

- Creating, listing, and deleting notebooks and entries.
- Saves into a flat file

## Flags

`--version` - displays current version of the app

## Commands

### Notebooks

__Current notebook__ - `kek notebook`

Shows current notebook being used. Default notebook is `default`

__List all notebooks__ - `kek notebook list`

Lists down all existing notebooks.

__Selecting a notebook__ - `kek notebook select <notebook name>`

You can select a notebook by using `select <notebook name>`. e.g., `kek notebook select my-notes`.
If notebook doesn't exist, it will create the notebook first and will select it.

__Deleting a notebook__ - `kek notebook remove <notebook name>`

You can delete a notebook by using `remove <notebook name>`. e.g., `kek notebook remove my-notes`.
NOTE: This will delete all notes in the specified notebook.


### Notes

__List all notes__ - `kek list`

Lists notes from selected notebook

__Adding a note__ - `kek add <note>`

Add a note to the selected notebook. e.g., `kek add "Created a draft for kek note specs"`.

__Removing a note__ - `kek remove <note>`

You can delete a note from the selected notebook by using `remove <note>` where `<note>` can be the note id or entry date. e.g., `kek remove 1` or `kek remove 20180218020059`.



