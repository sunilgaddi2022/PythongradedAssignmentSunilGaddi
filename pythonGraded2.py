import psutil



## Second question : Write a Python program to monitor the health of the CPU

def monitor_cpu_health(threshold=80):
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)  # Check CPU usage every 1 second

            if cpu_percent > threshold:
                print(f"Alert: CPU usage exceeded {threshold}% ({cpu_percent}%)")

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        # You can customize error handling for specific exceptions here.

if __name__ == "__main__":
    threshold = 80  # Set your desired threshold here
    print(f"Monitoring CPU usage (Threshold: {threshold}%)...")
    monitor_cpu_health(threshold)
