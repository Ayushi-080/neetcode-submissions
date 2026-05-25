class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sdict={}
        for i in nums:
            if i not in sdict:
                sdict[i]=1
            else:
                sdict[i]+=1
        for key,value in sdict.items():
            if value==1:
                return key
        