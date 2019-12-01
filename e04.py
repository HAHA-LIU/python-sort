'''快速排序'''
# 时间复杂度 O(n log n) 空间复杂度 O(log n)  不稳定
def sort(l):
    if len(l) < 2:
        return l
    mid = l[0]
    left = [i for i in l[1:] if i < mid]
    right = [i for i in l[1:] if i > mid]
    return sort(left) + [mid] + sort(right)

a = [23,33,44,12,55,12,8]
print(sort(a))

