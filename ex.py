"""
28/10/2017
b170448@cic.ipn.mx
badillo.soft@hotmail.com
github/badillosoft/python-scic
"""
#declare vars
listaPerrona,sumLst=[0,1,2,5,7,3,2],0
for i in listaPerrona:
    print(i,end='-')
    #sumLst of elements
    sumLst+=i
# get cardinality of list
n= len(listaPerrona)
#get avg
avg =sumLst/n
print("\nThe avg of lst is: " + str(avg))