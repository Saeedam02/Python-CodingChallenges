# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

#Approach 1: Merge Sort

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Calculate the Median of Two Sorted Arrays.

        :param num1: First input.
        :param nums2: Second inpu.

        :returns: the median of the two sorted arrays
        """
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0
        
        # Get the smaller value between nums1[p1] and nums2[p2].
        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans
        
        if (m + n) % 2 == 0:
            for _ in range((m + n) // 2 - 1):
                _ = get_min()
            return (get_min() + get_min()) / 2
        else:
            for _ in range((m + n) // 2):
                _ = get_min()
            return get_min()
        
nums1 = [1,3]
nums2 = [2]
c = Solution()
print(c.findMedianSortedArrays(nums1,nums2))

