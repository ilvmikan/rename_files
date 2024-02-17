import os
from pathlib import Path

user_directory = Path("~").expanduser()
folder_path = user_directory / "Pictures" / "icon"

for count, filename in enumerate(os.listdir(folder_path)):
    count += 1

    if not filename.startswith("icon_"): # checks that the file does not start with "icon"
        src = os.path.join(folder_path, filename) # stores directory and file
        dst = os.path.join(folder_path, "icon_" + str(count) + ".jpg") # directory + name of the file to be edited
        
        while os.path.exists(dst): # if the file name already exists, increase the "count" to create a unique name
            count += 1
            dst = os.path.join(folder_path, "icon_" + str(count) + ".jpg")
        
        os.rename(src, dst)

input('success! press enter')