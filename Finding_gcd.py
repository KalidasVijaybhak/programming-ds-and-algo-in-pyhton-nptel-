# brute force algorithm for finding gcd of a number using python



# the input will be given in the format gcd(m,n)


def gcd(m,n):
    fn = []  #array for storing factors of m
    cf = [] #array for storing the gcd        
    fm = [] #array for storing the factors of n
    for i in range(1,m+1):
        if m % i == 0 : 
            fm.append(i)
            
            
    for j in range(1,n+1):
        if n % j == 0 :
            fn.append(j)
            
            
            
    for f in fm:
        if f in fn :
            cf.append(f)
            
            
            
    return cf     





print(gcd(5,100))
