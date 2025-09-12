# Invert a Dictionary with Multiple Values
import copy

input_dict1 = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
# Output → {1: ['a', 'c'], 2: ['b', 'd'], 3: ['e']}
output = {}

for key, val in input_dict1.items():
    if val not in output:
        output[val] = [key]
    else:
        output[val].append(key)

print(output)
