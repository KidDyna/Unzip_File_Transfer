import zipfile
import os
import shutil
import os.path
import time
from glob import glob
from datetime import datetime

rootPath = 'zipData'
extractPath = 'rootPath\extracts'
DACDatabase = "DeluxeAreaCodeDatabase.csv"
fakeNDM = "new_path_fake_NDM_directory_for_file_transfer"


def extractFunc(fn):
    # Get a list of all archived file names from the zip
    with zipfile.ZipFile(r'fn', 'r') as zipObj:
        # Iterate over the file names
        listOfFileNames = zipObj.namelist()
        # Check filename endswith csv
        for fileName in listOfFileNames:
            # Extract a single file from zip
            if fileName.endswith('.csv'):
                zipObj.extract(fileName, r'{extractPath}')


def getFile(path_in, fn):
    return glob(os.path.join(path_in, fn))[0]


def renameFile(f, path_in, file_out):
    os.rename(f, os.path.join(path_in, file_out))


def copyTree(path_in):
    shutil.copytree(r'{extractPath}', r"{rootPath}\{path_in}", dirs_exist_ok=True)


# Create a ZipFile Object and load sample.zip in it
extractFunc('{rootPath}\zip-codes-database-STANDARD-csv.zip')

############ STILL NEED TO FIGURE OUT IDENTIFYING THE DELUXE AREA CODE DB ZIP WITH A WILDCARD INSTEAD OF YYYY-MM- ##############
extractFunc('{rootPath}\2022-03-DeluxeAreaCodeDatabase-csv.zip')

# Renames removes date prefix from Deluxe Area Code file
renameFile(getFile(extractPath, "*{DACDatabase}"), extractPath, DACDatabase)

dir_list = os.listdir(exractPath)
print("Files and directories in '", extractPath, "' :")
# prints all files
print(dir_list)

# Moves files to new folder
copyTree(fakeNDM)
copyTree('Dialer_Archive_For_Zip_Files')
# Adds Month / Year prefix to files for Archive purposes
date = datetime.now().strftime("%Y%m")
path = r'{rootPath}\Dialer_Archive_For_Zip_Files'

f = getFile(path, DACDatabase)
renameFile(f, path, f"{date}_{DACDatabase}")
f = getFile(path, "zip-codes-database-STANDARD.csv")
renameFile(f, path, f"{date}_zip-codes-database-STANDARD.csv")

# Creates trigger files after CSVs are placed in NDM
while not os.path.exists("{rootPath}/{fakeNDM}/{DACDatabase}"):
    time.sleep(1)

if os.path.isfile("{rootPath}/{fakeNDM}/{DACDatabase}"):
    for i in (1, 2):
        open("{rootPath}/{fakeNDM}/trigger{i}.txt", "w+")
else:
    raise ValueError("%s isn't a file!" % "{rootPath}/{fakeNDM}/{DACDatabase}")