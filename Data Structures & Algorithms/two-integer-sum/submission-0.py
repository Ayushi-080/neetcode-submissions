class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # res=[]
        # for i in range(0,len(nums)):
        #     for j in range(0,len(nums)):
        #         if nums[i]+nums[j]==target and i!=j:
        #             res.append(i)
        #             res.append(j)
        #             return res
        num_map={}
        for index in range(len(nums)):
            num=nums[index]
            complement=target-num
            if complement in num_map:
                return [num_map[complement],index]
            num_map[num]=index
        return num_map
