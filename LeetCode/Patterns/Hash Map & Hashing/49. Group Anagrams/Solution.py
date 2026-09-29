class Solution(object):
    def groupAnagrams(self, strs):

        groups = {}
        for n in strs:
            key = "".join(sorted(n))
            
            if key not in groups:
                groups[key] = []
            
            groups[key].append(n)
        
        return list(groups.values())

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        