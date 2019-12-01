'''选择排序'''
# 时间复杂度 O(n²) 空间复杂度 O(1)  不稳定
def sort(l):
    for i in range(len(l)-1):
        minindex = i
        for j in range(i+1,len(l)):
            if l[j] < l[minindex]:
                minindex = j
        if minindex != i:
            l[i],l[minindex] = l[minindex],l[i]
    return l

l = [3,2,8,1,5,6,9,7,10]
print(sort(l))

