# Nested Dictionary – Sum Values by Key

dict_list = [
    {'a': 10, 'b': 5},
    {'a': 3, 'b': 7, 'c': 4},
    {'a': 2, 'c': 1}
]
# Output → {'a': 15, 'b': 12, 'c': 5}
output = {}
for item in dict_list:
    for key,val in item.items():
        if key not in output:
            output[key] = val
        else:
            output[key] += val
print(output)