class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0

        # Left to Right
        open_count = close_count = 0
        for char in s:
            if char == '(':
                open_count += 1
            else:
                close_count += 1

            if open_count == close_count:
                max_length = max(max_length, 2 * close_count)
            elif close_count > open_count:
                open_count = close_count = 0  # reset counts

    # Right to Left
        open_count = close_count = 0
        for char in reversed(s):
            if char == ')':
                close_count += 1
            else:
                open_count += 1

            if open_count == close_count:
                max_length = max(max_length, 2 * open_count)
            elif open_count > close_count:
                open_count = close_count = 0  # reset counts

        return max_length
