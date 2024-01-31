# 345. Reverse Vowels of a String
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class Solution:
    def reverseVowels(self, s: str) -> str:
        rev_string = list(s)
        vowel = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}

        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start] in vowel and s[end] in vowel:
                rev_string[start], rev_string[end] = rev_string[end], rev_string[start]
                start += 1
                end -= 1
            else:
                if s[start] not in vowel: start += 1
                if s[end] not in vowel: end -=1
            
        return ''.join(rev_string)