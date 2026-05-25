from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        s1=Counter(s)
        t1=Counter(t)
        for k,v in s1.items():
            if s1[k]!=t1[k] or len(s)!=len(t):
                return False
        return True