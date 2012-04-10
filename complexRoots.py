import math
n=int(raw_input("Enter n: "))
precision = 4
number=complex(-1,0)
size=math.sqrt((number.real**2)+(number.imag**2))
root=1/n
mod=size**root
theta=0
arg=math.radians(360/n)
roots=[]
for i in range(0, n):
	x=round(mod*(math.cos(theta)),precision)
	y=round(mod*(math.sin(theta)),precision)
	roots.append(complex(x,y))
	theta=theta+arg
print roots
