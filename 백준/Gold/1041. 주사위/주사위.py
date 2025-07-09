import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print(sum(nums) - max(nums))

else:
    # 0-5, 1-4, 2-3 마주봄
    c2 = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    c3 = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]
    
    c1_min = min(nums)
    c2_min = min([nums[x] + nums[y] for x, y in c2])
    c3_min = min([nums[x] + nums[y] + nums[z] for x, y, z in c3])
    
    c1_cnt = (n - 1) * (n - 2) * 4 + (n - 2) ** 2
    c2_cnt = (n - 1) * 4 + (n - 2) * 4
    c3_cnt = 4
    
    print(c1_min * c1_cnt + c2_min * c2_cnt + c3_min * c3_cnt)