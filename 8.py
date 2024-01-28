import os
os.system("cls")

def roman_to_integer(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(s)):
        current_value = roman_values[s[i]]
        next_value = roman_values[s[i + 1]] if i + 1 < len(s) else 0

        if current_value < next_value:
            result -= current_value
        else:
            result += current_value

    return result

example1 = "III"
example2 = "LVIII"
example3 = "MCMXCIV"

output1 = roman_to_integer(example1)
output2 = roman_to_integer(example2)
output3 = roman_to_integer(example3)

print(f"Input: {example1}\nOutput: {output1}")
print(f"Input: {example2}\nOutput: {output2}")
print(f"Input: {example3}\nOutput: {output3}")