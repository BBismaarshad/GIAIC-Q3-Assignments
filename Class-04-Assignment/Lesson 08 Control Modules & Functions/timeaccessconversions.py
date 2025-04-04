import time

print(time.time())      # Current time in seconds since epoch
print(time.ctime())     # Current time as string
time.sleep(1)           # Sleep for 1 second

# Measure execution time
start = time.perf_counter()
# Code to measure here
end = time.perf_counter()
print(f"Elapsed: {end - start:.6f} seconds")