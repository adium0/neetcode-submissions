class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt=0
        alr=[]
        for i in range(len(nums)):
            if nums[i] not in alr:
                alr.append(nums[i])
            else:
                cnt+=1
        print(cnt)
        if cnt==0:
            return False
        else:
            return True