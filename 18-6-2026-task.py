# DAILY TASK- WEEK 3- DAY 1
'''
✓ Write @timer (execution time) and @logger (fn name + args) decorators
✓ Use lru_cache on fibonacci — compare time with @timer
✓ Use combinations to generate team fixtures from 5 teams
✓ Use groupby to group transactions by category
✓ Push to GitHub with a descriptive commit message'''
 
from functools import wraps, lru_cache
from itertools import combinations, groupby
import time

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\nCalling Function: {func.__name__}")
        print(f"Arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.6f} seconds")
        return result
    return wrapper

def fib_without_cache(n):
    if n < 2:
        return n
    return fib_without_cache(n - 1) + fib_without_cache(n - 2)

@lru_cache(maxsize=None)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n - 1) + fib_with_cache(n - 2)

print("\nFibonacci Comparison")
start = time.time()
result1 = fib_without_cache(30)
end = time.time()

print(f"Result: {result1}")
print(f"Total Time Without Cache: {end-start:.6f} seconds\n")

start = time.time()
result2 = fib_with_cache(30)
end = time.time()

print(f"Result: {result2}")
print(f"Total Time With Cache: {end-start:.6f} seconds")

print("\nTeam Fixtures")

teams = ["Team A", "Team B", "Team C", "Team D", "Team E"]

fixtures = combinations(teams, 2)

for match in fixtures:
    print(match)

print("\nTransactions Grouped By Category")

transactions = [
    ("Food", 200),
    ("Food", 150),
    ("Travel", 500),
    ("Travel", 700),
    ("Shopping", 1000),
    ("Shopping", 250)
]

transactions.sort(key=lambda x: x[0])

for category, items in groupby(transactions, key=lambda x: x[0]):
    print(f"\n{category}")

    for item in items:
        print(item)


@logger
@timer
def add(a, b):
    return a + b


print("\nDecorator Demo")
add(10, 20)