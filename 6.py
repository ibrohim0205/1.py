import os
os.system("cls")

def TwoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for k in range (i + 1, len(nums)):
            if nums[i] + nums[k] == target:
                return [i, k]