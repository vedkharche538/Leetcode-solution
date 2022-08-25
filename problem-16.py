"""
__summary__:Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

"""
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_map = {2: ['a', 'b', 'c'],
                    3: ['d', 'e', 'f'],
                    4: ['g', 'h', 'i'],
                    5: ['j', 'k', 'l'],
                    6: ['m', 'n', 'o'],
                    7: ['p', 'q', 'r', 's'],
                    8: ['t', 'u', 'v'],
                    9: ['w', 'x', 'y', 'z']}

        if len(digits) == 0:
            return []
        prod = dict_map[int(digits[0])]

        for i in range(1, len(digits)):

            prod = product(prod, dict_map[int(digits[i])])
            prod = ["".join(x) for x in prod]

        return prod
