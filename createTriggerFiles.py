import os.path
import time

while not os.path.exists("zipData/extracts/trigger1.txt"):
    time.sleep(1)

if os.path.isfile("zipData/extracts/trigger1.txt"):
    open("zipData/new_path_fake_NDM_directory_for_file_transfer/trigger1.txt","w+")
    open("zipData/new_path_fake_NDM_directory_for_file_transfer/trigger2.txt", "w+")
else:
    raise ValueError("%s isn't a file!" % "zipData/extracts/trigger1.txt")