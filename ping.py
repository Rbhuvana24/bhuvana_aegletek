
import subprocess

def ping_website(host):
    try:

        response = subprocess.run(
            ["ping", host],

            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if response.returncode == 0:
            print(f"{host} is reachable.")
            return True
        else:
            print(f"{host} is not reachable.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
if __name__ == "__main__":
    ping_website("www.google.com")


