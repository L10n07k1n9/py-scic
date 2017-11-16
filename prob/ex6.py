import matplotlib.pyplot as plt
file,l,X,Y,rowFloat=open("C:\\Users\\ld_la\\Google Drive\\IPN CIC MCC\\B17 MCC\\s1\\py\\prob\\resorte.csv","r"),[],[],[],[]
for line in file:
    row=line.split(",")
    rowFloat.append(list(map(lambda x: float(x),row)))
file.close()
X=list(map(lambda x: x[0],rowFloat))
Y=list(map(lambda x: x[1],rowFloat))
plt.plot(X,Y,"r--")
plt.show()
# print(X)
# print(Y)