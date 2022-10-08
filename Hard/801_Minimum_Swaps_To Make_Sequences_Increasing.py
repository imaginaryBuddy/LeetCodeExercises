"""
You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].

For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The test cases are generated so that the given input always makes it possible.

An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].
"""

class Solution(object):
    def minSwap(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        size = len(nums1)
        swap = [sys.maxsize] * size
        no_swap = [sys.maxsize] * size
        swap[0] = 1
        no_swap[0] = 0
        for i in range(1,size):
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                no_swap[i] = no_swap[i-1]
                swap[i] = swap[i-1] + 1

            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                swap[i] = min(no_swap[i-1]+1, swap[i])
                no_swap[i] = min(swap[i-1], no_swap[i])

        return min(swap[size-1], no_swap[size-1])
