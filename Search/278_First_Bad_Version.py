# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
    # idea: to use binary search
        l = 1 
        h = n 
        ver = 0 
        while (l <= h):
            mid = int((l+h)/2)
            bad = isBadVersion(mid)
            if (bad):
                # you have to save ver here, look at blog to see why 
                ver = mid
                h = mid-1 
            elif(not bad):
                l = mid+1

        return ver
        
