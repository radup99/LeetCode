class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lookup = [0] * n
        for num in nums:
            lookup[num-1] += 1
        return [i+1 for i in range(0, n) if lookup[i] == 0]
