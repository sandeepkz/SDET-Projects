# Merge Two Dictionaries

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
# Output → {'a': 1, 'b': 5, 'c': 7, 'd': 5}

for key,val in dict2.items():
    if key not in dict1:
        dict1[key] = val
    else:
        dict1[key] += val

print(dict1)