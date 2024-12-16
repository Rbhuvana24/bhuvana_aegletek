def create_config_file():
    # Prompt the user for input
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

if __name__ == "__main__":
    create_config_file()
