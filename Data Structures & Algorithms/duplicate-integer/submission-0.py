class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hash_set = set()

        for i in nums:
            if i in my_hash_set:
                return True
            else:
                my_hash_set.add(i)
        return False

        