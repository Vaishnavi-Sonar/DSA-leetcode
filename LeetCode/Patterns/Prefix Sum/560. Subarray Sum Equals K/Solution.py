class Solution(object):
    def subarraySum(self, nums, k):

        count = 0
        curr = 0
        seen = {0:1}

        for n in nums:
            curr += n

            if curr - k in seen:
                count += seen[curr-k]

            seen[curr] = seen.get(curr,0) + 1

        return count

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        