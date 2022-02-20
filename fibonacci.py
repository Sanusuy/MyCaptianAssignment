fib = int(input("enter the series: "))
a1,a2 = 0, 1
count = 0

if fib <= 0:
   print("Please enter a positive integer")

elif fib == 1:
   print("Fibonacci sequence upto",fib,":")
   print(a1)

else:
   print("Fibonacci sequence:")
   while count < fib:
       print(a1)
       nth = a1 +a2
       # update values
       a1 = a2
       a2 = nth
       count += 1