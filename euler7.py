#Euler 7
#find 10001st prime number 
import time
from math import sqrt
start=time.clock()
ps=[2,3]  #seed the list. 
pp = 3
while len(ps) < 10001:  
	pp+=2	#only want odds
	test=True
	sqrtpp=sqrt(pp)  #setup the square root condition for prime numbers
	for a in ps:
		if a>sqrtpp: break
		if pp%a==0:
		   test=False
		   break
	if test: ps.append(pp)

print ps[10000]
print time.clock()-start	