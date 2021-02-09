f selectionSort(l):
    for start in range(0,len(l)):
        minpos = start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos = i
        (l[start],l[minpos])=(l[minpos],l[start])
    return l     
        
        
l = [1,3,1,4,2,8,5]
print(selectionSort(l))
