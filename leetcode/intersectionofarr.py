'''
https://leetcode.com/problems/intersection-of-two-arrays
'''
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        z = n1.intersection(n2)

        return list(z)