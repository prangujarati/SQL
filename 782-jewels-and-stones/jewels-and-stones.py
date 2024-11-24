class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_cnt = 0
        for i in stones:
            if i in jewels:
                j_cnt = j_cnt + 1
        return j_cnt

        