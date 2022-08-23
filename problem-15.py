"""
summary: Longest Substring Of All Vowels in Order

A string is considered beautiful if it satisfies the following conditions:

Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).

For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.
Example 1:

Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
Example 2:

Input: word = "aeeeiiiioooauuuaeiou"
Output: 5
Explanation: The longest beautiful substring in word is "aeiou" of length 5.
Example 3:

Input: word = "a"
Output: 0
Explanation: There is no beautiful substring, so return 0.
"""


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        L, R = 0, 0
        output = 0
        length = 0
        # edge case: single letter strings1
        if(len(word) < 5):
            return 0
        if(word[0] != 'a'):
            while L < len(word) and word[L] != 'a':
                L += 1
            R = L
        hashmap = {}
        while R < len(word)-1:
            # process right element!
            # extend length of sliding window!
            length += 1
            char = word[R]
            hashmap[char] = R
            # good cases
            if(char == 'a' and (word[R+1] == 'a' or word[R+1] == 'e')):
                R += 1
                continue
            if(char == 'e' and (word[R+1] == 'e' or word[R+1] == 'i')):
                R += 1
                continue
            if(char == 'i' and (word[R+1] == 'i' or word[R+1] == 'o')):
                R += 1
                continue
            if(char == 'o' and (word[R+1] == 'o' or word[R+1] == 'u')):
                R += 1
                continue
            if(char == 'u' and (word[R+1] == 'u')):
                R += 1
                continue
            else:
                if('a' in hashmap and 'e' in hashmap and 'i' in hashmap and 'o' in hashmap and 'u' in hashmap):
                    output = max(output, length)
                # go to next valid sliding window!
                R += 1
                L = R
                length = 0
                hashmap = {}
        # edge case: longest beautiful substring is located at the end or is almost the entire string! R will always end
        # up at last index based on my while loop iteration up there!
        if(len(list(hashmap.keys()))) == 5 or (len(list(hashmap.keys())) == 4 and word[R] not in hashmap):
            output = max(output, length + 1)
        return output
