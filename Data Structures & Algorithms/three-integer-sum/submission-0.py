class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                temp=[a,nums[left],nums[right]]
                sum1=nums[i]+nums[left]+nums[right]
                if sum1==0:
                    res.append(temp)
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                elif sum1<0:
                    left+=1
                elif sum1>0:
                    right-=1
        return res
