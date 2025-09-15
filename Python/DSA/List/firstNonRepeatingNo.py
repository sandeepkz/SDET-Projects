# Input  → [9, 4, 9, 6, 7, 4]
# Output → 6

inp = [9, 4, 9, 6, 6, 4]
seen = {}
for num in inp:
    if num not in seen:
        seen[num] = 1
    else:
        seen[num] += 1

for num in inp:
    if seen[num] == 1:
        print(num)
        break
else:
    print(None)
    