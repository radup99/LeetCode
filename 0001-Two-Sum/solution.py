class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            x = target - nums[i]
            if x in nums:
                j = nums.index(x)
                if j != i:
                    return [i, j]
        return []
