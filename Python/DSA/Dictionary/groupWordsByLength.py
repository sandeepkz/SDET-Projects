# Group words by their length

words = ["apple", "bat", "car", "elephant", "dog", "banana"]
# Output → {5: ['apple'], 3: ['bat', 'car', 'dog'], 8: ['elephant'], 6: ['banana']}
output = {}

for item in words:
    ln = len(item)
    if ln not in output:
        output[ln] = [item]
    else:
        output[ln].append(item)
print(output)
