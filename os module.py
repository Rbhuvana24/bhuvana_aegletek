

import os
directory = input("Enter the directory path: ")
if os.path.exists(directory):
    print("Files in the directory:")
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            print(file)
else:
    print("The directory does not exist.")

