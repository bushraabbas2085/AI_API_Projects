import os
import shutil

base_folder = "Cleaner"

rules = {
    ".jpg" : "images" ,
    ".png" : "images" ,
    ".jpeg" : "images" ,
    ".pdf" : "Documents",
    ".docx" : "Documents",
    ".doc" : "Documents" ,
    ".txt" : "Documents",
    ".pptx" : "Slides" ,
    ".mp4" : "Videos" ,
    ".mkv" : "Videos",
    ".mp3" : "Audios" ,
    ".zip" : "Softwares",
    ".rar" : "Softwares",
    ".exe" : "Softwares"
}
all_files = os.listdir(base_folder)
print("Total files found :" , len(all_files))

for file in all_files:
    old_path = os.path.join(base_folder , file)
    if os.path.isfile(old_path):
        extension = os.path.splitext(file)[1].lower()
        if extension in rules:
            folder_name = rules[extension]
            new_folder_path = os.path.join(base_folder,folder_name)
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
                print('Created Folder :' , folder_name)
            new_path = os.path.join(new_folder_path , file)
            shutil.move(old_path , new_path)
            
            print(f'Moved {file} --->{folder_name}')

            
print("All Files Transferred")