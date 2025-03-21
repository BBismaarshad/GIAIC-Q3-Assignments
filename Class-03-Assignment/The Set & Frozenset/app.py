# Normal set with unique elements
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Set automatically removes duplicate elements
my_set = {1, 2, 2, 3, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing an element from the set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets (all elements from both sets)
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection of two sets (common elements)
print(set1 & set2)  # Output: {3}

# Difference of two sets (elements in set1 but not in set2)
print(set1 - set2)  # Output: {1, 2}

# Symmetric Difference (elements in either set but not in both)
print(set1 ^ set2)  # Output: {1, 2, 4, 5}

# Frozenset example
my_set = {1, 2, 3, 4}
frozen_set = frozenset(my_set)
print(frozen_set)  # Output: frozenset({1, 2, 3, 4})

# Frozenset as dictionary keys
frozen_set1 = frozenset({1, 2, 3})
frozen_set2 = frozenset({'a', 'b', 'c'})
my_dict = {
    frozen_set1: "Numbers",
    frozen_set2: "Letters"
}
print(my_dict)  # Output: {frozenset({1, 2, 3}): 'Numbers', frozenset({'a', 'c', 'b'}): 'Letters'}

# Frozenset is immutable, so adding/removing elements will raise an error
frozen_set = frozenset({1, 2, 3})
# frozen_set.add(4)  # This will raise an AttributeError
# frozen_set.remove(1)  # This will raise an AttributeError

# Frozenset operations (union, intersection, etc.)
frozen_set1 = frozenset({1, 2, 3})
frozen_set2 = frozenset({3, 4, 5})

# Union of two frozensets
union_set = frozen_set1.union(frozen_set2)
print("Union:", union_set)  # Output: Union: frozenset({1, 2, 3, 4, 5})

# Intersection of two frozensets
intersection_set = frozen_set1.intersection(frozen_set2)
print("Intersection:", intersection_set)  # Output: Intersection: frozenset({3})