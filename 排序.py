#coding=utf8
'''
import random
#生成随机数列
for i in range(13):
    A.append(random.randint(0, 1000))
'''

#随便一个数列,有重复数字391
A = [252, 229, 924, 391, 391, 375, 858, 909, 808, 585, 170, 771, 3, 458, 458]

print('原始数列:')
print(A)

#=============插入法========================
def sort_insert(A): 
    print("插入排序:")
    for i in range(len(A)):
        temp = A[i]
        del A[i]
        for j in range(i+1):
            count = 0
            if temp < A[j]:
                A.insert(j, temp)
                count = count + 1
                break
        if not count:
            A.insert(i, temp)  
    return A



#==============折半插入排序=========================
def Binary_Insertion_Sort(A):
    print("折半插入排序:")
    low = 0
    high = 0
    i = 0
    
    while i < len(A):
        mid = (low + high) // 2
        temp = A[i] #取出一个待排序的数
        del A[i]
        A_high = A[high]# 记下已排好的最大的数
        
        if temp >= A[low] and temp <= A[mid]: #待排序的数的范围
            for j in range(low, mid+1):
                if temp <= A[j]:
                    A.insert(j, temp)    
                    break
            
        elif temp > A[mid] and temp < A_high:
            for j in range(mid, high+1):
                if temp <= A[j]:
                    A.insert(j, temp)    
                    break     
               
        elif temp >= A_high:
            A.insert(high+1, temp)
            
        else:
            A.insert(low, temp)
            
        high = high + 1 #已排好的队列增加一个 
        i = high + 1 #选择下一个待排列的数
        
    return A


#======================归并排序=====================
def separate(L):#将数列分成两个左右部分
    long = len(L)
    half = int(long / 2)
    left = L[:half]
    right = L[half:]
    return left, right

def merge(left,right):#合并已经排好序的两个数列
    result=[]#新建一个数列
    l = 0 
    r = 0
    while (l < len(left) and r < len(right)): 
        if left[l] < right[r]:#将比较小的数放到result中
            result.append(left[l])
            l = l + 1
        else:
            result.append(right[r])
            r = r + 1
    result = result + left[l:]#放好剩下的数
    result = result + right[r:]
    return result

def merge_sort(A):
    if len(A) < 2:#数列个数不够2个的不要排序,直接返回
        return A 
    else:
        left, right = separate(A)#分成左右两个部分
        sorted_left = merge_sort(left)#递归地排序左边
        sorted_right = merge_sort(right)#递归地排序右边
        merged = merge(sorted_left, sorted_right)#合并两个已经排好的数列
        return merged
        
        
 
#======================堆排序=====================
#--------------------网上的答案--------------------------
def heap_sort(lst):
    print("堆排序:")
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    # 堆排序
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst


##======================快速排序=====================
#快速排序是原地排序
#--------------算法导论的例子------------------
#网上找的好像有错误,已经改正了
def Quick_Sort_book(A):
    print("快速排序--算法导论的例子:")
    
    def partion(array, p, r):# 选一个数组作为中元, 放在中间
        key = array[r] #选数组最后一个数字作为中元
        i = p #i是第0个数
        for j in range(i, r):  #从第一个数开始
            if array[j] <= key:  #如果数字比中元小,就放在左边
                array[i], array[j] = array[j], array[i]
                i = i + 1  
        array[i], array[r] = array[r], array[i]  #将中元和比他大的第一个数交换, 中元放到中间
        return i   
    
    def quick_sort(array, p, r):# p:数组开始的下标, r:数组结束的下标
        if p < r:
            q = partion(array, p, r)
            quick_sort(array, p, q - 1)
            quick_sort(array, q + 1, r)
        return array    
    
    quick_sort(A, 0, len(A) - 1)
    return A

    
#--------------------网上的答案--------------------------
def Quick_Sort_net(A):
    print("快速排序--网上的答案:")
    
    def quickSort(L, low, high):
        i = low
        j = high
        if i >= j:
            return L
        key = L[low] #将第一个数作为中元
        while i < j:
            while i < j and L[j] >= key:#把比中元小的放左边
                j = j - 1
            L[i] = L[j]
            while i < j and L[i] <= key:#把比中元大的放右边
                i = i + 1
            L[j] = L[i]
        L[i] = key#中元放中间
        quickSort(L, low, i - 1)
        quickSort(L, j + 1, high)
        return L    

    quickSort(A, 0, len(A) - 1)
    return A



#============希尔排序============================

def ShellSort(A):
    print("希尔排序:")
    
    def up_int(N):#向上取整
        if N ==1 :
            return 0
        n = N // 2
        if n *2 < N:
            return n+1
        else:
            return n
        
    def switch(L, gap ): #将第i个数和第i+gap个元素比较
        for i in range(len(L)-gap):
            if L[i] > L[i+gap]:
                L[i], L[i+gap] = L[i+gap], L[i]
        return L
 
    lenth  = len(A)
    gap = up_int(lenth)
    while (gap > 0):
        switch(A, gap)
        gap = up_int(gap) 
    return A


#=====================冒泡排序=====================
def bubble(A):
    print("冒泡:")
    lenth  = len(A)
    for i in range(lenth):#比较冷(A)-1次
        for j in range(lenth-1):#和旁边的比较
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


#=======================简单选择排序========
def Select_Sort(A):
    print("简单选择排序:")
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A


#===============外部排序===========
'''
外部排序指的是大文件的排序，即待排序的记录存储在外存储器上，
待排序的文件无法一次装入内存，需要在内存和外部存储器之间进行多次数据交换，
以达到排序整个文件的目的。外部排序最常用的算法是多路归并排序，
即将原文件分解成多个能够一次性装入内存的部分，分别把每一部分调入内存完成排序。
然后，对已经排序的子文件进行多路归并排序。
'''

#===============基数排序===========
#-------------可能写成了桶排序-----
def radix_sort(A):
    print("基数排序:")
    
    large = 0
    for i in range(len(A)):#找出最大的数
        if A[i] > large:
            large = A[i]
    max_bits = 0
    while large // 10**max_bits:#找出最大的数的位数
        max_bits = max_bits+1        
    
    MList = []    
    for i in range(10): #创建一个多维数组
        MList.append([])
    
    for i in range(max_bits):#每一位进行一次排序
        for j in range(len(A)):#把一个位的数提取出来, 放到对应的临时二维数组中
            n = A[j] // 10**i % 10
            MList[n].append(A[j])
        A = []#把原来的数组清零
        for m in range(10): #从临时数组中把数字按顺序取出, 返回原来的数组,完成一次排序  
            for num in MList[m]:
                A.append(num)
        MList = []  #把临时数组清零      
        for i in range(10): #创建一个多维数组
                MList.append([])  
       
    return(A)
    
    
#===============计数排序===========    
def counting_soft(A):
    print("计数排序:")
    
    large = 0
    for i in range(len(A)):#找出最大的数
        if A[i] > large:
            large = A[i]
    
    C = [0] * (large + 1)#建一个辅助数列
    output = []#输出数列
    
    for i in A:#算数列里每个数的出现次数
        C[i] = C[i] + 1
    
    for j in range(large+1):
        if C[j]:
            for r in range(C[j]):#按出现次数放回输出数列
                output.append(j)
    return output
            
    
print(sort_insert(A))
print(Binary_Insertion_Sort(A))
print("归并排序:")
print(merge_sort(A))
print(heap_sort(A))
print(Quick_Sort_book(A))
print(Quick_Sort_net(A))
print(ShellSort(A))
print(Select_Sort(A))
print(bubble(A))
print(radix_sort(A))
print(counting_soft(A))