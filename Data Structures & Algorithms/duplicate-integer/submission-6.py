class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for item in nums:
            hashset.add(item)

        return not (len(hashset) == len(nums))