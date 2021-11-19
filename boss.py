# -*- coding: utf-8 -*-
# @Time    : 2021/11/9 7:50 下午
# @Author  : zhengjiawei
# @FileName: boss.py
# @Software: PyCharm

str1 = 'abcd'
str2 = 'ababc'


# 'abc'

# 求公共子串

def common_str(str1, str2):
    sub_str = set()
    sub_str_list = []
    # 记录str1中所有子串
    for each in str1:
        if each not in sub_str:
            sub_str.add(each)
            sub_str_list.append(''.join(sub_str))
        else:
            sub_str = set()
            sub_str.add(each)
            sub_str_list.append(''.join(sub_str))
    reslut = []
    for each in sub_str_list:
        if each in str2:
            reslut.append(len(each))
        else:
            reslut.append(0)

    return sub_str_list[max(reslut).index()]


def find_sub_str(s1, s2):
    short,long = (s1,s2) if len(s1)<s2 else (s2,s1)
    sub_str = ''
    for i in range(len(short)):
        for j in range(len(short)):
            if short[i:j+1] in long and j+1-i >len(sub_str):
                sub_str = short[i:j+1]
    return sub_str

    # short, long = (s1, s2) if len(s1) < len(s2) else (s2, s1)
    #
    # repeat = ''
    #
    # for i in range(len(short)):
    #     for j in range(len(short)):
    #         if short[i:j + 1] in long and j + 1 - i > len(repeat):
    #             repeat = short[i:j + 1]
    #     print(repeat)
    # return repeat


if __name__ == '__main__':
    repeat = find_sub_str(str1, str2)
    print(repeat)
