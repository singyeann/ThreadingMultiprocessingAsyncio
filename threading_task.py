import threading
import time

def simulate_io_task(task_name, duration):
    print(f"Starting {task_name}...")
    time.sleep(duration)  # Simulating blocking I/O operation
    print(f"{task_name} completed.")

def run_io_tasks():
    threads = []
    tasks = [("Task 1", 2), ("Task 2", 3), ("Task 3", 1)]
    
    for task_name, duration in tasks:
        thread = threading.Thread(target=simulate_io_task, args=(task_name, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to complete
