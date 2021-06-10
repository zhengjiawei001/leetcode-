# -*- coding: utf-8 -*-

class Solution:
    def sortSentence(self, s: str) -> str:
        s_dict = {}
        for each in s.split(' '):
            s_dict[each[-1]] = each[:-1]
        s_list = []
        s_dict = sorted(s_dict.items(), key=lambda item: item[0])
        for _, value in s_dict:
            s_list.append(value)
        return ' '.join(s_list)


class Solution_1:
    def sortSentence(self, s: str) -> str:
        s = s.split(' ')
        len_ = len(s)
        s_list = [''] * len_
        for each in s:
            s_list[int(each[-1]) - 1] = each[:-1]
        return ' '.join(s_list)


if __name__ == '__main__':
    solution = Solution()
    s = "is2 sentence4 This1 a3"
    print(solution.sortSentence(s))
    solution_1 = Solution_1()
    print(solution_1.sortSentence(s))
