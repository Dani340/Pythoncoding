n =input("n= ")
sum = 0
while n > 0:
	sum = sum + n % 10
	print(n % 10)
	n /= 10
print (sum)

