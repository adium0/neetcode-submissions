class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        numset=set(nums)
        for i in nums:
            if i-1 not in numset:
                length=0
                while i+length in numset:
                    length+=1
                res=max(length,res)

        return res