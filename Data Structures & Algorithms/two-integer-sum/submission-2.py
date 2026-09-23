class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        complements = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complements:
                return [complements[complement], i]
            else:
                complements[nums[i]] = i
                