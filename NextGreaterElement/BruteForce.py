class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ary_res = []
        for i in nums1:
            print("----"+str(i))
            idx = nums2.index(i)
            if idx == len(nums2)-1:
                ary_res.append(-1)
                continue         
            else:
                for j in range(idx, len(nums2)):
                    print(nums2[j])
                    if nums2[j] >i:
                        ary_res.append(nums2[j])
                        break
                    if j==len(nums2)-1:
                        ary_res.append(-1)

        return ary_res
                
