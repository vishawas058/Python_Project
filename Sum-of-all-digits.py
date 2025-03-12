#input from user
n = int(input("Enter The Number: "))
r = 0
s = 0
#while loop
while(n != 0):
  r = n % 10
  s = s + r
  n //= 10
#print sum
print("Sum of the digits are",s)
