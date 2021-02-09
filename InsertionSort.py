def insertionSort(l):
    for sliceEnd in range(len(l)):
        pos = sliceEnd
        while pos>0 and l[pos]<l[pos-1]:
            (l[pos],l[pos-1])=(l[pos-1],l[pos])
            
        pos = pos-1
    return l    
    
k = [1,3,1,4,2,8,5]
print(insertionSort(k))    
