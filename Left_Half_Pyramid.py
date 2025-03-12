#Take input from user
n=int(input("Enter The Number: "))
#Outer Loop
for i in range(1,n+1):
	#First Inner Loop
	#Print Space
  for j in range(1,n-i+1):
    print(" ",end=" ")
	#Second Innet Loop
	#Print Stars
  for j in range(1,i):
    print("*",end=" ")
#For New Line
  print("")
