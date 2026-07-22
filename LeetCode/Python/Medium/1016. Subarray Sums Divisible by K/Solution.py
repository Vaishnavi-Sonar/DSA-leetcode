class Solution(object):
    def subarraysDivByK(self, nums, k):

        curr = 0
        count = 0
        seen = {0:1}

        for n in nums:
            curr += n
            rem = curr % k
            
            if rem in seen:
                count += seen[rem]
            seen[rem] = seen.get(rem, 0) + 1
        
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        