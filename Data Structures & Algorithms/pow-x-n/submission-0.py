class Solution:
    def myPow(self, x: float, n: int) -> float:
        bf=n
        ans=1
        if n<0:
            x=1/x
            bf=-bf
        while bf>0:
            if bf%2==1:
                ans=ans*x
            x=x*x
            bf=bf//2
        return ans
        
        