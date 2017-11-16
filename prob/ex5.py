# File csv stores in 1st line X values, 2nd line = Y
import matplotlib.pyplot as pl
# Program which ask the user the name of file
sFile= input("File? ")
# Open in read mode
f=open(sFile,"r")
# Get 2 lines splitted by ","
X=list(map(lambda x:float(x),f.readline().split(",")))
Y=list(map(lambda x:float(x),f.readline().split(",")))

f.close()
# Get X,Y SERIESs
pl.plot(X,Y,"r--")
# plot
pl.show()