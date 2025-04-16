from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for n, i in enumerate(nums):
        for m, j in enumerate(nums):
            if n == m:
                continue
            if i + j == target:
                return [n, m]

# for test
# print(twoSum([2,7,11,15], 9))
