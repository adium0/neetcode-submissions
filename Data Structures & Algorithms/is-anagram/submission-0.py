class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=collections.defaultdict(int)
        t1=collections.defaultdict(int)
        a=len(s)
        b=len(t)
        if a!=b:
            return False
        for i in s:
            s1[i]+=1
        for i in t:
            t1[i]+=1
        
        if s1==t1:
            return True
        return False

