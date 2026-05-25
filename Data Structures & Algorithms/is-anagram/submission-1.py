class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # res=False
        # if (len(s)==len(t)):
        #     s1="".join(sorted(s))
        #     t1="".join(sorted(t))
        #     if s1==t1:
        #         res=True
        # return res
        d1={}
        for i in s:
            if i in d1:
                d1[i]=d1[i]+1
            else:
                d1[i]=1
        
        d2={}
        for i in t:
            if i in d2:
                d2[i]=d2[i]+1
            else:
                d2[i]=1
        if d1==d2:
            return True
        else:
            return False
