class Solution(object):
    def findMaxLength(self, nums):

        prefix = [nums[0]]
    
        curr = 0
        ans = 0
        seen = {0:-1}

        for i, n in enumerate(nums):
            if n == 0:
                curr -= 1
            else:
                curr += 1
            
            if curr in seen:
                ans = max(ans, i - seen[curr])
            else:
                seen[curr] = i
        
        return ans



        """
        :type nums: List[int]
        :rtype: int
        """
        