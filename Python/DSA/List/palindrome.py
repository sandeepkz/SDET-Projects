# list is palindrome

input1 = [1, 2, 3, 2, 4]
# Output → True

for i in range(len(input1)//2):
    if input1[i] != input1[-(i+1)]:
        print('not palindrome')
        break
else:
    print('palindrome')