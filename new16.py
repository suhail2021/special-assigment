def evenodd(A): 
   evenlist = [] 
   oddlist = [] 
   for i in A: 
      if (i % 2 == 0): 
         evenlist.append(i) 
      else: 
         oddlist.append(i) 
   print("Even lists:", evenlist) 
   print("Odd lists:", oddlist) 
  
 
A=list()
n=int(input("Enter the size of the First List "))
print("Enter the Element of First  List ")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
evenodd(A) 





