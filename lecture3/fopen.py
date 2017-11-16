#map matrix from csv file
f=open("file.csv","r")

def Cast2Int(el):
    return int(el,10)
mat=[]
for lineOfFile in f:
    sRow=lineOfFile.split(",")
    iCast=list(map(Cast2Int,sRow))
    mat.append(iCast)

print(mat)
