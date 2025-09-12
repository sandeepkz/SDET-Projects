# Sort a Dictionary by its Values

input_dict = {'a': 3, 'b': 1, 'c': 2}
# Output → {'b': 1, 'c': 2, 'a': 3}
output = {}
sortedVal = sorted(input_dict.values())

for num in sortedVal:
    for key, val in input_dict.items():
        if num == input_dict[key]:
            output[key] = num
print(output)

# Another way --->
sortedDict = sorted(input_dict.items(), key=lambda x:x[1])

print(dict(sortedDict))