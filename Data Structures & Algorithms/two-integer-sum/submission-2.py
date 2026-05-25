class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i=0
        # j=len(nums)-1
        # while i<j:
        #     if nums[i]+nums[j]==target:
        #         return [i,j]
        #     elif nums[i]+nums[j]>target:
        #             j=j-1
        #     elif nums[i]+nums[j]<target:
        #             i=i+1
        hashmap={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]]=i
           