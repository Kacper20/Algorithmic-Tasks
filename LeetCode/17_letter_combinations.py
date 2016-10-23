class Solution(object):
    def letterCombinations(self, digits):

        def helper(dict, result, temp_string, digits, index):
            if len(temp_string) == len(digits):
                if len(temp_string) != 0:
                    result.append(temp_string)
                return
            current_char = digits[index]
            for character in dict[current_char]:
                helper(dict, result, temp_string + character, digits, index + 1)

        dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        result = []
        helper(dict, result, '', digits, 0)
        return result
