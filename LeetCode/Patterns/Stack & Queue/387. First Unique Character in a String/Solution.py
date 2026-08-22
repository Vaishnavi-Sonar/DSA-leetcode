class Solution(object):
    def firstUniqChar(self, s):

        count = {}

        for c in s:
            count[c] = count.get(c,0)+1
        
        for i,n in enumerate(s):
            if count[n] == 1:
                return i
                
        return -1
        

        """
        :type s: str
        :rtype: int
        """
        