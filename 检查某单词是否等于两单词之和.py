# -*- coding: utf-8 -*-

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        if self.str2num(firstWord)+self.str2num(secondWord)==self.str2num(targetWord):
            return True

        else:
            return False

    def str2num(self, str_):
        lis = [chr(i) for i in range(97, 123)]
        str2num_dict = {each: str(i) for i, each in enumerate(lis)}
        result = []
        for each in str_:
            result.append(str2num_dict[each])
        return int(''.join(result))
