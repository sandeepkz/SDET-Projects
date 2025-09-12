# Find the Most Frequent Element in a List

nums = [1, 2, 2, 3, 1, 4, 2]
# Output → 2   (because it appears 3 times, the most)

dict1 = {}
for num in nums:
    if num not in dict1:
        dict1[num] = 1
    else:
        dict1[num] += 1

count = 0
highest = None
for key in dict1:
    if dict1[key] > count:
        highest = key
        count = dict1[key]

print(highest)
