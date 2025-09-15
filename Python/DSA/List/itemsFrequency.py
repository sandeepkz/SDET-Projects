# Input  → ['a', 'b', 'a', 'c', 'b', 'a']
# Output → {'a': 3, 'b': 2, 'c': 1}

Input = ['a', 'b', 'a', 'c', 'b', 'a']
Output = {}
for num in Input:
    if num not in Output:
        Output[num] = 1
    else:
        Output[num] += 1
print(Output)