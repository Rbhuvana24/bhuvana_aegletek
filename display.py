import time
duration = 60
interval = 10
start_time = time.time()
print("Displaying system time every 10 seconds for one minute:")
while time.time() - start_time < duration:
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"Current System Time: {current_time}")
    time.sleep(interval)
print("Finished displaying system time.")
