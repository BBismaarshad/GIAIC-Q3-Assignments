import random

print(random.random())        # Random float between 0.0 and 1.0
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(['a', 'b', 'c']))  # Random choice from sequence
random.shuffle([1,2,3,4])     # Shuffles list in place
print(random.uniform(1.5, 4.5)) # Random float between 1.5 and 4.5