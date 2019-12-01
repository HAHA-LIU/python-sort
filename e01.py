'''冒泡排序'''
# 时间复杂度 O(n²) 空间复杂度 O(1)  稳定
def sort(l):
    for i in range(1,len(l)):
        for j in range(0,len(l)-i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

l = [3,2,8,1,5,6,9,7,10]
print(sort(l))



