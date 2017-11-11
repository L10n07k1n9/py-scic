mat=[
    [1,2,3],
[4,5,6],
[7,8,9,10]
]

f=open("mat2.csv","w")
#cast param to string
def T(x):
    return str(x)

for row in mat:
    sRow= map(T,row)
    line=",".join(sRow)+"\n"
    f.write(line)

f.close

print(":".join(["a","b","c"]))
print("***".join(["a","b","c"]))