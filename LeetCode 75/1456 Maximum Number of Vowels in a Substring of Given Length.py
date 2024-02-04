# 1456. Maximum Number of Vowels in a Substring of Given Length

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

class Solution:
    
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        current_sum = sum([1 for x in s[:k] if x in vowel])
        max_val = current_sum

        for r in range(k, len(s)):
            if s[r-k] in vowel : current_sum -= 1
            if s[r] in vowel : current_sum += 1
            max_val = max(max_val, current_sum)

        return max_val