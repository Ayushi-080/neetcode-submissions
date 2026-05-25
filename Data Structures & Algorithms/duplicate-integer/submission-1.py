from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        l=Counter(nums)
        for k,v in l.items():
            if v>1:
                return True
        return False