import os
from tkinter import *
from idlelib import Scrol

"""
This script is intended to backup your files to a specified location and
shut down the computer after completion. 

Upon first use, a GUI will prompt the user to select:
- A directory to be backed up (including all contents)
- A directory to store back up files (overwrites prexisting content that changed)

A simple, yet effective effort at keeping your data safe.
"""

class Window():
    def __init__(self, master):
        self.sc = ScrolledCanvas(root,highlightthickness=0, takefocus=1)
        self.sc.frame.pack(expand=1, fill="both", side="left")
        self.item = FileTreeItem(os.getcwd())
        self.node = TreeNode(sc.canvas, None, item)
        self.node.expand()

# Check for a directory location file called 'backup_locations.config'
try:
    with open('backup_locations.config') as file:
        print(file.readlines())
except:
    # If no file exists:
        # Open a GUI to choose a backed up directory
        root = Tk()
        window = Window(root)
        root.mainloop()

        # Open a GUI to choose a saving directory

        # Write the .config file for both directories for consecutive uses

# Ask user if they want to shut down

# Copy backed up directory to saving directory

# Shut down, if applicable
