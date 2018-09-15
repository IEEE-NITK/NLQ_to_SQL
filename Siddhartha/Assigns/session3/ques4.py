#Write a program to delete alternate entries in a list

mylist=[0,1,2,3,4,5,6,7]
l=len(mylist)
for i in range(0,l):
	if(i >= len(mylist)):
		break
	del mylist[i]
print(mylist)