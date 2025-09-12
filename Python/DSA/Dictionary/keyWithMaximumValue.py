# Find the Key with the Maximum Value

input_dict = {'a': 10, 'b': 25, 'c': 8}
# Output → 'b'   (because 25 is the largest value)

highestKey = highestVal = float('-inf')

for key, val in input_dict.items():
    if val > highestVal:
        highestVal = val
        highestKey = key

print(highestKey)
