import os

def check_and_create_directory(directory_path):

    if not os.path.exists(directory_path):
        print(f"Directory does not exist. Creating: {directory_path}")
        os.makedirs(directory_path)
    else:
        print(f"Directory already exists: {directory_path}")
folder_path ="C:/Users/bhuva/OneDrive/Documents"
check_and_create_directory(folder_path)
