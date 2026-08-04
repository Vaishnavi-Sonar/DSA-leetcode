class Solution(object):
    def sortedSquares(self, nums):

        return sorted(list(n*n for n in nums))
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        