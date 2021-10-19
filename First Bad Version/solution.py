# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        up = n
        down = 1
        while up>=down :
            mid = (up+down)//2
            res = isBadVersion(mid)
            if res==True:
                up = mid-1           
            else:
                down= mid+1
           
        return down
