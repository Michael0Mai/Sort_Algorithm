#coding=utf8


class Mini_Heap():#用数组表示
    def __init__(self):
        self.data = [] #一定有数据
        self.size = 0 #数据的个数
        self.level = 0 #树的层数
        
    def creat(self, A):#创建堆
        for i in A:
            self.data.append(i)
        self.adjust()
        
    def levels(self):
        L = 0
        number = 2**L
        while number < self.size :
            L = L+1
            number = number + 2**L
        return L    
    
    def adjust(self): #排好数据的顺序   
        n = 0
        self.size = len(self.data) #数据的个数
        self.level = self.levels() #树的层数
        for i in range(self.level):#算出最右边的节点序号
            n = n + 2**i
        while n >=0:#从底向上比较
            self._adjust(n)
            n = n - 1
    
    def _adjust(self, i):
        #维护节点和两个子节点的数据结构
        if i >= 0 and 2*i +1 < self.size:
            if self.data[2*i+1] < self.data[i]:
                self.data[2*i+1], self.data[i] = self.data[i], self.data[2*i+1] 
            if 2*i +2 < self.size and self.data[2*i+2] < self.data[i]:
                self.data[2*i+2], self.data[i] = self.data[i], self.data[2*i+2]   
        else:        
            return None
        #递归维护两个子节点
        self._adjust(2*i+1) 
        self._adjust(2*i+2)
        
    def insert(self, element): #插入新数字
        self.data.append(element)
        self.size = self.size +1
        # 向上过滤节点, 只和父节点比较,比用self.adjust()重新逐个维护子树的结构少做无用的比较
        i = self.size-1
        while i > 0 and self.data[int((i-1)/2)] > element:
            self.data[i] = self.data[int((i-1)/2)]
            i = int((i-1)/2)
        self.data[i] = element
            
    
    def delete(self): #堆只会删除第一个
        if len(self.data) > 0:
            #把堆最后一个数放到根节点
            mini_number = self.data[0]
            self.data[0] = self.data[self.size-1]
            temp = self.data[0]
            del self.data[self.size-1]
            #和两个子节点比较, 向下层层过滤
            parent = 0 
            while parent <= int((self.size-3)/2):
                child = 2*parent+1
                if self.data[child] > self.data[child+1]:
                    child = child + 1
                
                if self.data[child] > temp:
                    break
                else:
                    self.data[parent] = self.data[child]
                    parent = child
            if len(self.data) > 0: #删除一个后, 要再次检查堆的大小
                self.data[child] = temp
        else:
            mini_number = None
        return mini_number
    
    def find_mini(self):
        return self.data[0]
        
        
        
#======================================================    
def test():
    A = [252, 229, 924, 391, 375, 858, 909, 808, 585, 170, 771, 3, 458, 235, 818, 919]
    A = [252, 229, 924, 391, 375, 858, 909]  
    A = []
    
    heap = Mini_Heap()
    heap.creat(A)
    print(heap.data)
    
    heap.insert(270)
    print(heap.data)
    
    print(heap.delete())
    print(heap.data)
    
test()