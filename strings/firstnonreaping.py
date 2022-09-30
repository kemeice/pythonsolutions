#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

#Example 1:

#Input: s = "leetcode"
#Output: 0
#Example 2:

#Input: s = "loveleetcode"
#Output: 2
#Example 3:

#Input: s = "aabb"
#Output: -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for key , letter in enumerate(s):
            c = s.count(letter)
            if c ==1:
                return key
        return -1