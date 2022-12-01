class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0 
        s = list() 
        total = len(nums1) + len(nums2)
        median = total / 2 
        i = 0
        while (i < int(median) + 1):
            if p1 >= len(nums1) :
                s.append(nums2[p2])
                p2+=1
            elif p2 >= len(nums2) :
                s.append(nums1[p1])
                p1 +=1 
            elif nums1[p1] >= nums2[p2] :
                s.append(nums2[p2])
                p2 +=1 
            elif nums2[p2] > nums1[p1] :
                s.append(nums1[p1])
                p1+=1 

            i+=1

        if total % 2 == 0 :
            print("even")
            return (s[-1] + s[-2])/2
        else :
            return s[-1]  

Console
