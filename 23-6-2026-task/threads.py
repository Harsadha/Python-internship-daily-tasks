# DAILY TASK- WEEK 3- DAY 4
'''
✓ Fetch 5 URLs sequentially — measure time
✓ Repeat with ThreadPoolExecutor — compare time
✓ Use Lock to safely write results to shared log
✓ Write pytest suite for BankAccount (Day 3) with parametrize
✓ Mock an external API call and test the dependent function
'''

print("\nDay 14 task on concurrency and testing...\n")

# fetching sequentially (without threadpoolexecutor)
import requests
import time

urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums",
    "https://jsonplaceholder.typicode.com/todos"]

start = time.time()

for url in urls:
    requests.get(url)

end = time.time()

print("Time taken for sequential fetches:\n",end-start)
print()

# fetching url using threadpoolexecutor
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    return requests.get(url)

start = time.time()

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(fetch,urls)
    
end = time.time()

print("Time taken for fetch using threadpoolexecutor:\n",end-start)
print()

# lock to safely write into shared log
print("Using lock to write in logs..\n")
from threading import Lock

lock = Lock()

def fetch(url):
    response=requests.get(url)
    with lock:
        with open("shared_log.txt","a") as file:
            file.write(f"{url}->{response.status_code}\n")

# same threadpoolexecutor is used
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(fetch,urls)

print("Finished writing to the log.")

# pytest suite for bankaccount class with parametrize
