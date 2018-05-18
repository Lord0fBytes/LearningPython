import time

'''
Exercise 5.2
'''

tTime = time.time()
edtTime = tTime-(4*3600)
days = int(edtTime/86400)
hours = (edtTime-(days*86400))/3600
mins = (hours-int(hours))*60
secs = (mins-int(mins))*60
strSecs = ""
if(secs < 10):
	strSecs = "0"+str(int(secs))
else:
	strSecs = str(int(secs))

print(f"Exercise 5.1: Days: {int(days)}, {int(hours)}:{int(mins)}:{strSecs} EDT")

'''
Exercise 5.2
'''
print("Exercise 5.2")
a,b,c,n = 0,0,0,0

def check_fermat(a,b,c,n):
	if n>2 and a**n+b**n==c**n:
		print(f"Holy smokes, Fermat was wrong!")
	else:
		print(f"No, that doesn’t work. {a**n}+{b**n}={a**n+b**n} != {c**n}")

a=int(input("A:"))
b=int(input("B:"))
c=int(input("C:"))
n=int(input("N:"))

check_fermat(a,b,c,n)


'''
Exercise 5.3
'''
print("Exercise 5.3")

a,b,c = 0,0,0
def is_triangle(a,b,c):
 	if a+b>c and b+c>a and a+c>b:
 		print("Yes")
 	else:
 		print("No")

a=int(input("A:"))
b=int(input("B:"))
c=int(input("C:"))

is_triangle(a,b,c)

'''
Exersice 5.4

Not doing as it is not really programming.
'''