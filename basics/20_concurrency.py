# Concurrency is the ability to manage multiple requests at the same time, but not necessarily executing them simultaneously.
# Instead the system switches between the requests
# 	This is useful because if certain task is waiting the system can switch to another task and continue executing it.

import threading
import time

def process_request(request_id):
    print(f"Processing request {request_id}")
    time.sleep(3)
    print(f"Request {request_id} processed")

threads = []

for i in range(5):
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()