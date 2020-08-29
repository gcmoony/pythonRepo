import os
import tkinter as tk
from tkinter.filedialog import askdirectory

'''
With minor adjustments done to two existing packages of Google Photos Takeout, I'm somewhat confident that this
program will work at moving all image and video files out of their individually dated folders. A lot of 
directories store .json files for configuration things I suppose, so I try to isolate those files from 
my exclusive search. 

To use this project, you will need a few things:

1. A Google account with Photos uploaded to photos.google.com
2. A directory where you want to move your downloaded photos to

To begin, start by visiting takeout.google.com

Next, log into your account, then choose the data you would like to export.
Since this program is mostly catered towards a specific set of data, your photos,
I would advice using this program on one particular set of data as all files moved
are simply put into one directory.

Click "Next step", and choose your frequency. I would choose "Export once".

Click "Create export". Depending on how large your export is, you may get an email instead
of an instant download link. 

If prompted, click "Download" next to your export. You should now have a zip file with
the name "takeout-(exportID)-(exportSegmentNumber).zip"

Unzip the file, and now you should have a "Takeout" folder.

Now, using this program, you can start moving photos into a 
separate directory.

Be sure to always choose the "Google Photos" directory that will be found after unzipping
your data.
'''




def mainScreen():

    # Functions 
    def get_main_directory():
        directory = askdirectory()
        main_entry.insert(0, directory)

    def get_storage_directory():
        directory = askdirectory()
        storage_entry.insert(0, directory)

    def files_moved_message():
        tk.Label(
            window,
            text = "Moving Files"
        ).grid(row = 3, column = 1, padx = 5)

    window = tk.Tk()
    window.title("Takeout File Mover")

    # Open Main Directory
    open_main = tk.Button(
        window,
        text = "Open Google Photos directory...",
        #padx = 10,
        command = get_main_directory
    )
    main_entry = tk.Entry(
        window,
        width = 50
    )

    # Open Storage Directory
    open_storage = tk.Button(
        window,
        text = "Open storage directory...",
        command = get_storage_directory
    )
    storage_entry = tk.Entry(
        window,
        width = 50
    )

    # Move Files
    move_files = tk.Button(
        window,
        text = "Move Files",
        padx = 20,
        pady = 20,
        command = lambda: [moveFiles(main_entry.get(), storage_entry.get()), files_moved_message()]
    )

    # Organizing Items
    open_main.grid(row= 0, column = 0, sticky = "ew", padx = 5)
    main_entry.grid(row= 0, column = 1, sticky = "e", padx = 5)
    open_storage.grid(row= 1, column = 0, sticky = "ew", padx = 5)
    storage_entry.grid(row= 1, column = 1, sticky = "e", padx = 5)
    move_files.grid(row=3, column = 0, padx = 5)


    window.mainloop()


def moveFiles(main_directory, storage_directory):
    # Variables n stuff
    file_ext_avoid = [".json"] # File extensions you want to ignore
    curr_dir_files = [] # This variable stores current directory items, such as folders and text files
    dupe_count = 0 # In case you have two similarly named files, this will allow you to rename a duplicate name and still save whatever file it was

    os.chdir(main_directory)
    curr_dir_files = os.listdir()
    try:
        os.mkdir(storage_directory)
    except:
        # This just means the directory was already created
        pass
    for a_dir in curr_dir_files:
        os.chdir(main_directory + "\\" + a_dir)
        working_dir = os.listdir()
       
        for afile in working_dir:
            for extention in file_ext_avoid:
                if extention not in afile.lower():
                    # Duplicate Image name stuff
                    try:
                        os.rename(afile, storage_directory + "\\" + afile)
                    except:
                        os.rename(afile, storage_directory + "\\" + "dupe_of_" + str(dupe_count) + afile)
                        dupe_count += 1

def main():
    mainScreen()
   

if __name__ == '__main__':
    main()