import os
os.system("cls")

def is_palindrome(x):
    if x < 0:
        return False

    original_number = x
    reversed_number = 0

    while x != 0:
        digit = x % 10
        reversed_number = reversed_number * 10 + digit
        x //= 10

    return original_number == reversed_number

example1 = 121
example2 = -121
example3 = 10

output1 = is_palindrome(example1)
output2 = is_palindrome(example2)
output3 = is_palindrome(example3)

print(f"Input: {example1}\nOutput: {output1}")
print(f"Input: {example2}\nOutput: {output2}")
print(f"Input: {example3}\nOutput: {output3}")