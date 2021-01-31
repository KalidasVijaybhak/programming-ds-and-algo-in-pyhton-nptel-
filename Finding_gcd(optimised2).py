#simplidied version of finding gcd level 2


#if it is asked only to find the largest gcd its best to loop from largest to smallest than the other way




def gcd(m,n):
    cf = 1
    i = min(m,n)
    while i > 0:
        if(m%i ==0) and (n%i == 0):
            return(i)
        else:
            i = i-1
            
 
    
    
    
print(gcd(10,15))
