import os
os.system("cls")

def has_single_continuous_segment(s):
    ones_count = 0
    continuous_segments = 0

    for char in s:
        if char == '1':
            ones_count += 1
        else:
            ones_count = 0

        if ones_count > 1:
            continuous_segments += 1

    return continuous_segments == 1


input_str1 = "011100"
input_str2 = "11101"

output_str1 = "yes" if has_single_continuous_segment(input_str1) else "no"
output_str2 = "yes" if has_single_continuous_segment(input_str2) else "no"

print(f"Input : {input_str1}\nOutput : {output_str1}")
print(f"Input : {input_str2}\nOutput : {output_str2}")