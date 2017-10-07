num=int(input("Enter Number:"))
factor = 1
if num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factor = factor*i
   print("The factorial of",num,"is",factor)
