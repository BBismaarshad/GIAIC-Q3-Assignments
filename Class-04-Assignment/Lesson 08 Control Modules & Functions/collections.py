from collections import Counter, defaultdict, deque, namedtuple

# Counter
count = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(count)  # Counter({'a': 3, 'b': 2, 'c': 1})

# defaultdict
d = defaultdict(int)
d['a'] += 1
print(d['a'])  # 1 (default 0 for missing keys)

# deque
q = deque([1,2,3])
q.append(4)
q.appendleft(0)
print(q)  # deque([0, 1, 2, 3, 4])

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # 10 20