# Find all duplicates in a list while keeping the original order.

input_list = [1, 2, 3, 2, 4, 5, 1, 6, 2]
# Output → [2, 1]

seen = set()
dup = set()
output = []
for num in input_list:
    if num not in seen:
        seen.add(num)
    elif num not in dup:
        dup.add(num)
        output.append(num)
print(output)



