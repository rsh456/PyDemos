class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        max_val = -1
        for i in nums:
            if i in majority:
                majority[i]=majority[i]+1
                
            else:
                majority[i]=0
        result = 0
        for k,v in majority.items():
            if max_val < v:
                max_val = v
                result = k
        return result
        
