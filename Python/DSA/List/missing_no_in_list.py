# Find the Missing Number in a List of 1…n

nums = [3, 7, 1, 2, 8, 4, 5]
# Output → 6
counter = 1
len1 = len(nums) + 1
set1 = set(nums)
while counter <= len1:
    if counter not in set1:
        print(counter)
    counter += 1

# another way
nums = [3, 7, 1, 2, 8, 4, 5]

n = len(nums) + 1                  # should be 8
expected_sum = n * (n + 1) // 2    # formula for sum(1..n)
actual_sum = sum(nums)             # sum of given list
missing = expected_sum - actual_sum

print(missing)  # 6

