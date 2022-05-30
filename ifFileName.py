import os
import re
import zipfile

filenames = os.listdir('zipData\.')
for filename in filenames:
    if re.findall(r"DeluxeAreaCodeDatabase-csv", filename):
        print(filename)
        break

    if not filename:
        print("No file found")
