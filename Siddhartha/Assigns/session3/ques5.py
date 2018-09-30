#implementing quicksort
"""
def mypartition(A,p,r):
	pivot=A[r]
	i=p
	for j in range(p,r-1):
		if A[j]<= pivot :
			A[j],A[i]=A[i],A[j]
			i=i+1
	A[i],A[r]=A[r],A[i]
	return i

def myquicksort(A,p,r):
	if p >= r:
		return
	q=mypartition(A,p,r)
	myquicksort(A,p,q-1)
	myquicksort(A,q+1,r)
"""
mylist=[]
for i in range(0,6):
	mylist.append(int(input("enter the elements :")))
mylist.sort()
print(mylist)

