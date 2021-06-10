# -*- coding: utf-8 -*-
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        s_num = 0
        for i in range(len(s) - 2):
            if len({s[i], s[i + 1], s[i + 2]}) == 3:
                s_num += 1
        return s_num


if __name__ == '__main__':
    solution = Solution()
    s = "aababcabc"
    print(solution.countGoodSubstrings(s))
