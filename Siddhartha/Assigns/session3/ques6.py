#Write a program to generate the following pattern for any n
#spaces not included

n=int(input("enter the val of n:"))

for i in range(1,n+1):
	for j in range(0,2*i-1):
		print("*",end="")
	print("")
for i in range(n-1,0,-1):
	for j in range(0,2*i-1):
		print("*",end="")
	print("")