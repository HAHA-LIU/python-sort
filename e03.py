'''插入排序'''
# 时间复杂度 O(n²) 空间复杂度 O(1)  稳定
def sort(l):
    for i in range(len(l)):
        j = i-1
        key = l[i]
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j-=1
        l[j+1] = key
    return l

l = [2,3,8,1,5,6,9,7,10]
print(sort(l))


