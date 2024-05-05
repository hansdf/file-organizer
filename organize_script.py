import os
from pathlib import Path
import shutil

#check where this script is being ran from
original_folder = Path.cwd()

#list of folders I want to create to organize the files
imgs_folder = original_folder / "imgs_folder"
docs_folder = original_folder / "docs_folder"
exes_folder = original_folder / "exes_folder"
midia_folder = original_folder / "midia_folder"
misc_folder = original_folder / "misc_folder"

#check if the folders already exist, else it will create then
for folder in [imgs_folder, docs_folder, exes_folder, midia_folder, misc_folder]:
    if not folder.exists():
        folder.mkdir(mode=0o777, parents=True) #the folders were being created in 'read only' mode, 
                                               #so this is the solution I found after searching for it

for file in original_folder.iterdir():
    if file.is_file(): 

        # find out what is the file extension
        extension = file.suffix.lower()

        # move the file to the corresponding folder based on its extension
        if extension in [".jpeg", ".jpg", ".gif", ".png"]:
            shutil.move(str(file), str(imgs_folder / file.name))
        elif extension in [".txt", ".docx", ".doc", ".pdf"]:
            shutil.move(str(file), str(docs_folder / file.name))
        elif extension == ".exe":
            shutil.move(str(file), str(exes_folder / file.name))
        elif extension in [".mkv", ".mp4", ".mp3"]:
            shutil.move(str(file), str(midia_folder / file.name))
        elif extension in [".py"]:
            pass
        else:
            shutil.move(str(file), str(misc_folder / file.name))


input("\nPRESS ENTER TO EXIT")
