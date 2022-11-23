#Given two strings s and t, determine if they are isomorphic.
#Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

# ************** CODE ************

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            x = list(set(zip(s,t)))
            for i in range(len(x)):
                for j in range(len(x)):
                    if x[i][0] == x[j][0]:
                        if x[i][1] != x[j][1]:
                            return False
                            break
                        elif i == len(x)-1:
                            return True
                    elif x[i][0] != x[j][0]:
                        if x[i][1] == x[j][1]:
                            return False
                            break
 # The code took overal 83 ms to execute.
