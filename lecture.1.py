estatura=1.63
masa=57
IMC=estatura/(masa**2)
if IMC < 25:
    print("bajo de peso")
elif IMC < 30:
    print("peso normal")
elif IMC < 35:
    print("casi bien")
else:
    print("peso alto")

a,b,c,n=0,0,0,0
range(a,b,n) #step	
range(n,n)
range(1,101,2) # limite 101-1
	
def ex1():
    sum1=0
    for i in range(1,20+1):
        sum1=sum1+(i+1/i+2)**3
    return sum1
def ex2():
    sum2=0
    for i in range(100,1000+1):
        sum2=sum2+((1/i)**2)
    return sum2
	
def ex3():
    sum3=0
    for i in range(2,8+1):
        sum3=sum3+((i-(i**2))**4)
    return sum3


