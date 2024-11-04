#Leetcode tasks

#leetcode task 1
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp += 1
                res = max(res, temp)
            else:
                temp = 1

        return res

#leetcode task 2
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a = m-1
        b = n-1
        c = m+n-1

        while b>=0:
            if a>=0 and nums1[a]>nums2[b]:
                nums1[c] = nums1[a]
                a-=1
            else:
                nums1[c] = nums2[b]
                b-=1
            c-=1

#leetcode task 3
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        res = set1 & set2

        return list(res)