class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lst = [-1]
        valid = 0
        for i, char in enumerate(s):
            if char == '(':
                lst.append(i)
            else:
                lst.pop()
                if lst:
                    valid = max(valid,i - lst[-1])
                else:
                    lst.append(i)
        return valid
        
        