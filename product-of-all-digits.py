#input from user
n = int(input("Enter The Number: "))
r = 0
p = 1
#while loop
while(n != 0):
  r = n % 10
  p *= r
  n //= 10
#print product
print("Product of the digits are",p)
