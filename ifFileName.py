import os

filenames = os.listdir("zipData")
for filename in filenames:
     if "DeluxeAreaCodeDatabase-csv.zip".lower() in filename.lower():
         print(filename)