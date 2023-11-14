class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)>1:
                nums.remove(i)
                for j in nums:
                    if nums.count(j)>1:
                        nums.remove(j)
        return len(nums)
