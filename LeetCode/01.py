#class Solution:
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(0,len(nums)-1):
        for j in range(1, len(nums)):
            if i == j:
                continue
            if nums[i]+nums[j] == target:
                return [i, j]

#Solution()
print(twoSum([2,5,5,11],10))