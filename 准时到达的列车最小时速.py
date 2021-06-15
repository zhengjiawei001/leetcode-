# -*- coding: utf-8 -*-
import math


# 暴力循环求解
class Solution:
    def minSpeedOnTime(self, dist, hour: float) -> int:
        seed_lower = 10 ** 9
        if len(dist) - 1 > hour:
            seed_lower = -1
        else:
            for i in range(1, 10 ** 7 + 1):
                # print(max(dist))
                sum_ = 0
                for j in range(len(dist) - 1):
                    sum_ += math.ceil(dist[j] / i)
                # print(sum_)
                sum_ += dist[-1] / i

                if math.ceil(sum_ * 100) / 100 == hour:
                    # print(i)
                    if seed_lower > i:
                        seed_lower = i

        return seed_lower


# 使用二分法
class Solution_0:
    def minSpeedOnTime(self, dist, hour: float) -> int:

        if len(dist) - 1 >= hour:
            return -1

        def check_seed(v):
            h = 0
            for d in dist[:-1]:
                h += math.ceil(float(d) / v)
            h += float(dist[-1]) / v
            return h <= hour

        l, r = 1, 10 ** 7
        while l < r:
            mid = (l + r) // 2
            if check_seed(mid):
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    dist = [1, 1, 100000]
    hour = 2.01
    solution = Solution()
    solution_0 = Solution_0()
    print(solution.minSpeedOnTime(dist, hour))
    print(solution_0.minSpeedOnTime(dist, hour))
