# Find a Subarray with a Given Sum

nums = [1, 5, -3, 10, 5]
target = 12
# Output → [2, 3, 7]

ln = len(nums)
for i in range(ln-1):
    total = 0
    for j in range(i, ln):
        total += nums[j]
        if total == target:
            print(nums[i:j+1])


