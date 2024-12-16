import logging
import os
def read_log_file(file_path: str) -> None:
    try:
        with open(file_path, 'r') as log_file:
            print("Displaying log file contents:\n")
            for line_number, line in enumerate(log_file, start=1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    abspath=os.path.abspath('password.py')
    print(abspath)
    read_log_file(abspath)
