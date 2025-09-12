num = "12321"

def palindrome(num):
    return num == num[::-1]

print(palindrome("1212"))

"""
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
"""