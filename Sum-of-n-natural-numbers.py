#Sum of N natural Numbers
#Take input from usre
n = int(input("Enter the Number"))
sum = 0
#Using While Loop
while n >= 1:
	sum += n
	n -= 1
print("Sum of total number is",sum)
