# Find pairs in a list that sum to a given number

nums = [2, 4, 3, 7, 1, 5, 9]
target = 10
ln = len(nums)
output = []
# Expected Output → [(3, 7), (1, 9)]
for i in range(ln-1):
    for j in range(i+1, ln):
        if nums[i] + nums[j] == target:
            output.append((nums[i],nums[j]))
