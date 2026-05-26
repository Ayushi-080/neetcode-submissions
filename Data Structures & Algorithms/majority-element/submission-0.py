from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        l=len(nums)//2
        d=Counter(nums)
        for k,v in d.items():
            if d[k]>l:
                return k
