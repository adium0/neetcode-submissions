class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res=[-1,-1]
        reslen=float('inf')
        l=0
        count={}
        countT={}
        for i in t:
            countT[i]=1+countT.get(i,0)
        have=0
        need=len(countT)
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            if s[r] in countT and count[s[r]]==countT[s[r]]:
                have+=1
            
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                count[s[l]]-=1
                if s[l] in countT and count[s[l]] < countT[s[l]]:
                    have-=1
                
                l+=1
            
        l,r=res
        return s[l:r+1] if reslen!=float('inf') else ""