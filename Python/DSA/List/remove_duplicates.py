# Write a function to remove duplicates from a list while keeping order.

input_list = [1, 2, 2, 3, 4, 3, 5]
# output = [1, 2, 3, 4, 5]
seen = set()
output = []
for i in input_list:
    if i not in seen:  # here checking in seen() because it is faster & time complexity is O(1)
        seen.add(i)
        output.append(i)
print(list(output))

# set searches by hash table and directly jumps to element so time complexity is O(1)
# list scan element one by one so time complexity is O(n)
