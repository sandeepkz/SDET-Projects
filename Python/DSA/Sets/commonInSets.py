set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Expected Output → {3, 4}

print(set1.intersection(set2))
exp = set()
for num in set1:
    if num in set2:
        exp.add(num)
print(exp)