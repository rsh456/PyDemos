class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = []
        for i in range (0,3):
            for j in nums:        
                if j==i:
                    tmp.append(j)
                
        for i in range(0,len(tmp)):
            nums[i]=tmp[i]
