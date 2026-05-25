class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res=False
        if (len(s)==len(t)):
            s1="".join(sorted(s))
            t1="".join(sorted(t))
            if s1==t1:
                res=True
        return res
