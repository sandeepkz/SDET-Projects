# swap two tuples

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Output → t1 = (4, 5, 6), t2 = (1, 2, 3)

t3 = t1
t1, t2 = t2, t1

print(t1)
print(t2)