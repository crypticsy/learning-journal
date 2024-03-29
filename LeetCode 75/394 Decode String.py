# 394. Decode String

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 
# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].



class Solution:
    def decodeString(self, s: str) -> str:
        output = ""
        
        i = 0
        while i < len(s):
            
            if s[i].isdigit():
                start = i
                i+=1
                while s[i] != '[': i += 1
                digit = int(s[start:i])

                start = i+1
                i += 1

                count = 1
                while i < len(s):
                    if s[i] == '[': count += 1
                    if s[i] == ']': count -= 1
                    if s[i] == ']' and count == 0: break
                    i += 1
                
                word = self.decodeString(s[start:i])
                output += word * digit

            else:
                output += s[i]

            i+=1

        return output