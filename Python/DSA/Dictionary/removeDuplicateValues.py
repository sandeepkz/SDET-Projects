# Remove Duplicate Values from a Dictionary
from collections import Counter

input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# new_dict = {1:2, 2:1, 3:1}
# Output → {'b': 2, 'd': 3}
new_dict = {}
output = {}

for key,val in input_dict.items():
    if val not in new_dict:
        new_dict[val] = 1
    else:
        new_dict[val] += 1

for key, val in input_dict.items():
    if new_dict[val] == 1:
        output[key] = val

print(output)

value_count = Counter(input_dict.values())
print(value_count)