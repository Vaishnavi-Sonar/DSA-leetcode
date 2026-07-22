class Solution(object):
    def pivotIndex(self, nums):

        total = sum(nums)
        left = 0

        for i, n in enumerate(nums):
            right = total - left - n

            if right == left:
                return i
            left += n
        
        return -1


        """
        :type nums: List[int]
        :rtype: int
        """
        