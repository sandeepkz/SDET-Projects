# Python program to swap keys and values in a dictionary.

input_dict = {'a': 1, 'b': 2, 'c': 3}
# Output → {1: 'a', 2: 'b', 3: 'c'}
new_dict = {}

for key,val in input_dict.items():
    new_dict[val] = key

print(new_dict)