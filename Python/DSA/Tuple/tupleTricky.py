t = (10, 20, 30, 40, 50)
"""
Tasks:

Unpack first two values into separate variables (a, b) and rest into a list rest.
👉 Expected Output → a=10, b=20, rest=[30, 40, 50]

Swap the first and last elements using tuple unpacking.
👉 Expected Output → (50, 20, 30, 40, 10)
"""

a = t[0]
b = t[1]
rest = list(t[2:])

print(a, b, rest)

t = (t[-1],) + t[1:-1] + (t[0],)
print(t)
