class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ME = None
        count = 0
        for i in nums:
            if count==0:
                ME = i
            
            if ME!=i:
                count -=1
            else:
                count+=1
            
        return ME
