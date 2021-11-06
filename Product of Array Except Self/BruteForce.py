class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
     
        for i in range(0, len(nums)):
            res_t = 1
            for a in range(0,i):
                res_t= nums[a]*res_t
            for b in range(i+1,len(nums)):
                res_t = nums[b]*res_t
            res.append(res_t)
        return res
