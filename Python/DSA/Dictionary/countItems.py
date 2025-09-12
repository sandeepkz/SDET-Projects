# Count the frequency of each element in a list
nums = [1, 2, 2, 3, 1, 4, 2]
# Output → {1: 2, 2: 3, 3: 1, 4: 1}
dict1 = {}

for num in nums:
    if num not in dict1:
        dict1[num] = 1
    else:
        dict1[num] += 1

print(dict1)
