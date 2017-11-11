xo,yo,vox,voy,g=10,20,20,15,9.81
print("{} | {} | {}".format("t","x","y"))
for i in range(0,31):
    t=i/10
    x=vox*t+xo
    y=-g*t**2/2+voy*t+yo

    f="{:03.2f} | {:3.2f} | {:3.2f}".format(t,x,y)
    print(f)

