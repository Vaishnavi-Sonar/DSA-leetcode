class Solution(object):
    def twoSum(self, numbers, target):
        seen = {}
        for i,n in enumerate(numbers):
            complement = target - n
            if complement in seen:
                return [seen[complement]+1, i+1]
            seen[n] = i

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        