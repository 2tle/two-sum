from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i==j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]

# for test
print(twoSum([2,7,11,15], 9))