def fib(n):
    a=-1
    b=1
    while True:
      if n==0:
          return
      else:
          c=a+b;
          yield c
          a=b
          b=c
          n=n-1
    
##i=fib(6)
##Snext(i)
