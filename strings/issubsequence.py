#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#Example 1:

#Input: s = "abc", t = "ahbgdc"
#Output: true
#Example 2:

#Input: s = "axc", t = "ahbgdc"
#Output: false
 
 def isSubsequence(self, s: str, t: str) -> bool:
        remainder_of_t = iter(t)
        for letter in s:
            if letter not in remainder_of_t:
                
                return False
        return True
       