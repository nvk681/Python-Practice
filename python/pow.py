def myPow(self, x, n):
        if(n==0):
            return 1.0
        if(n<0):
            x = 1/x
        n = abs(n)
        xval = x*x
        return myPow(xval, n//2) if(n%2 == 0) else x*myPow(xval, n//2)