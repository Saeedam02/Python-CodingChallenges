# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# class Median(object):
#     def __init__(self)

def findMedianSortedArrays(self, nums1:list, nums2:list) ->float :
    """
    Calculate the Median of Two Sorted Arrays.

    :param num1: First input.
    :param nums2: Second inpu.

    :returns: the median of the two sorted arrays
    """
    m = len(nums1)
    n = len(nums2)
    nums1.append(nums2)
#     m = len(nums1)
#     n = len(nums2)
#     if m > n: return self.findMedianSortedArrays(nums2, nums1)
#     low = 0
#     high = m
#     while low <= high:
#         midIndex = (low + high)/2
#         x = nums1[midIndex]
#         y = nums2[midIndex - low]
#         if x < y:
#             low = midIndex + 1
#         elif x > y:
#             high = midIndex - 1
#         else:
#             if midIndex == 0 or nums1[midIndex-1] != x:
#                 return float(x)
#         low = midIndex + 1
#         high = min(len(nums2), midIndex + 1)
#         left_half = max(0, midIndex - low)
#         right_half = min(high, len(nums1))
#         total_length = left_half + right_half
#         if total_length % 2 == 0:
#             return (max(left_half, right_half) * x + min(right_half, left_half) * y)
#         else:
#             return float((max(left_half, right_half) * x + min(right_half, left_half) * y)
#                          / (total_length + 1))
# print(findMedianSortedArrays([1,3],[5]))
nums1 = [1,3]
nums2 = [2]
