class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = strs[0]
        for i in strs:
            prefixLength = min(len(i),len(longestPrefix))
            while i[0:prefixLength] != longestPrefix[0:prefixLength]:
                prefixLength = prefixLength -1
            longestPrefix = i[0:prefixLength]
            
        return longestPrefix