'''
Problem3: Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

'''

actual_string = input()
pattern = input()


def is_match(actual_string, pattern):
    if len(actual_string) == 0 and len(pattern) == 0:
        return True
    elif len(actual_string) == 0 and len(pattern) > 0:
        return False
    elif len(actual_string) > 0 and len(pattern) == 0:
        return False
    elif len(actual_string) > 0 and len(pattern) > 0:
        if pattern[0] == '.':
            return is_match(actual_string[1:], pattern[1:])
        elif pattern[0] == '*':
            return is_match(actual_string[1:], pattern[1:]) or is_match(actual_string[1:], pattern) or is_match(actual_string, pattern[1:])
        elif pattern[0] == actual_string[0]:
            return is_match(actual_string[1:], pattern[1:])
        else:
            return False
    else:
        return False


result = is_match(actual_string, pattern)
print(result)
