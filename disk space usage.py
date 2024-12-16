import shutil

# Program to create a configuration file based on user input

def create_config_file():
    server_name = input("Enter the server name: ")
    ip_address = input("Enter the IP address: ")
    config_content = f"""[Server]
Name = {server_name}
IP = {ip_address}
"""
    file_name = "server_config.txt"

    try:
        with open(file_name, "w") as config_file:
            config_file.write(config_content)
        print(f"Configuration file '{file_name}' has been created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the configuration file: {e}")

def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)

    print(f"Total Disk Space: {total_gb:.2f} GB")
    print(f"Used Disk Space: {used_gb:.2f} GB")
    print(f"Free Disk Space: {free_gb:.2f} GB")
if __name__ == "__main__":
    create_config_file()
    print("\nDisk Space Usage:")
    check_disk_space()
