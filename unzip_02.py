import zipfile
import os
import shutil

# Create a ZipFile Object and load sample.zip in it
with zipfile.ZipFile(r'C:\Users\kiddy\Documents\GitHub\unzip_file_transfer\Unzip_File_Transfer\zipData\zip-codes-database-STANDARD-csv.zip', 'r') as zipObj:
    # Get a list of all archived file names from the zip
    listOfFileNames = zipObj.namelist()
    # Iterate over the file names
    for fileName in listOfFileNames:
        # Check filename endswith csv
        if fileName.endswith('.csv'):
            # Extract a single file from zip
            zipObj.extract(fileName, r'C:\Users\kiddy\Documents\GitHub\unzip_file_transfer\Unzip_File_Transfer\zipData\extracts')

############ STILL NEED TO FIGURE OUT IDENTIFYING THE DELUXE AREA CODE DB ZIP WITH A WILDCARD INSTEAD OF YYYY-MM- ##############

with zipfile.ZipFile(r'C:\Users\kiddy\Documents\GitHub\unzip_file_transfer\Unzip_File_Transfer\zipData\2022-03-DeluxeAreaCodeDatabase-csv.zip', 'r') as zipObj:
    # Get a list of all archived file names from the zip
    listOfFileNames = zipObj.namelist()
    # Iterate over the file names
    for fileName in listOfFileNames:
        # Check filename endswith csv
        if fileName.endswith('.csv'):
            # Extract a single file from zip
            zipObj.extract(fileName, r'C:\Users\kiddy\Documents\GitHub\unzip_file_transfer\Unzip_File_Transfer\zipData\extracts')

# Renames removes date prefix from Deluxe Area Code file
from glob import glob
path = r'C:\Users\kiddy\Documents\GitHub\unzip_file_transfer\Unzip_File_Transfer\zipData\extracts'
f = glob(os.path.join(path, "*DeluxeAreaCodeDatabase.csv"))[0]
os.rename(f, os.path.join(path, "DeluxeAreaCodeDatabase.csv"))

dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# prints all files
print(dir_list)

# Moves files to new folder

shutil.copytree(r"C:\Users\kiddy\Documents\GitHub\unzip_file_transfer\Unzip_File_Transfer\zipData\extracts",r"C:\Users\kiddy\Documents\GitHub\unzip_file_transfer\Unzip_File_Transfer\zipData\new_path_fake_NDM_directory_for_file_transfer", dirs_exist_ok=True)
shutil.copytree(r"C:\Users\kiddy\Documents\GitHub\unzip_file_transfer\Unzip_File_Transfer\zipData\extracts",r"C:\Users\kiddy\Documents\GitHub\unzip_file_transfer\Unzip_File_Transfer\zipData\Dialer_Archive_For_Zip_Files", dirs_exist_ok=True)

# Adds Month / Year prefix to files for Archive purposes

from glob import glob
from datetime import datetime

date = datetime.now().strftime("%Y%m")
path = r'C:\Users\kiddy\Documents\GitHub\unzip_file_transfer\Unzip_File_Transfer\zipData\Dialer_Archive_For_Zip_Files'
f = glob(os.path.join(path, "DeluxeAreaCodeDatabase.csv"))[0]
os.rename(f, os.path.join(path, f"{date}_DeluxeAreaCodeDatabase.csv"))
f = glob(os.path.join(path, "zip-codes-database-STANDARD.csv"))[0]
os.rename(f, os.path.join(path, f"{date}_zip-codes-database-STANDARD.csv"))
