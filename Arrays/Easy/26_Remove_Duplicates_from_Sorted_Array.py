class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        i = 1
        j = 1
        while (j < size):
            if nums[j] == nums[j-1]:
                j+=1
            else:
                nums[i] = nums[j]
                j+=1
                i+=1

        return i
