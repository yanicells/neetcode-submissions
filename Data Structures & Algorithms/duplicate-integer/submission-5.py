class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set = []
        for i in range(len(nums)):
            if not (nums[i] in set):
                set.append(nums[i])

        return not (len(nums) == len(set))
        