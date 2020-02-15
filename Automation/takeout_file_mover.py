import os


'''
With minor adjustments done to two existing packages of Google Photos Takeout, I'm somewhat confident that this
program will work at moving all image and video files out of their individually dated folders. A lot of 
directories store .json files for configuration things I suppose, so I try to isolate those files from 
my exclusive search. 
'''

def main():
    # Variables n stuff
    main_directory = "D:\\Some Example Directory\\takeout-xxexampletakoutfolderxx\\Takeout\\Google Photos\\" # Could add double '\' so no modifiers accidentally occur
    storage_directory = "D:\\Some Example Directory\\" + "Moved Files\\" # Where you wanna store your pictures and stuff
    file_ext_avoid = [".json"] # File extensions you want to ignore
    curr_dir_files = [] # This variable stores current directory items, such as folders and text files
    dupe_count = 0 # In case you have two similarly named files, this will allow you to rename a duplicate name and still save whatever file it was


    os.chdir(main_directory)
    #print(os.getcwd())
    curr_dir_files = os.listdir()
    #print(curr_dir_files)
    try:
        os.mkdir(storage_directory)
    except:
        # This just means the directory was already created
        pass
    for a_dir in curr_dir_files:
        os.chdir(main_directory + a_dir)
        working_dir = os.listdir()

        for file in working_dir:
            print(file)
            
            for extention in file_ext_avoid:
                if extention not in file.lower():
                    # Duplicate Image name stuff
                    try:
                        os.rename(file, storage_directory + file)
                    except:
                        os.rename(file, storage_directory + str(dupe_count) + file)
                        dupe_count += 1

        #for extention in file_extension:
        #    if extention in item.upper() or extention in item.lower():
        #        os.rename(item, storage_directory + item)
        #        int(item_counter)
        #        item_counter += 1
# + file_prefix + (str(item_counter))

if __name__ == '__main__':
    main()