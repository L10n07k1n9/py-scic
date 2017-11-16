import math
# initial position and initial speed
A = 10
j = 1
# ellasticity const
k = 3
# mass
m = 1


def f(x):
    w = (k / m)**0.5
    return A * math.sin(w * t + j)


# linear space to graph (sucession sequence) vars
n = 100
t_min = 0
t_max = 4

file_out = open("resorte.csv", "w")

for i in range(n):
    t = t_min + (t_max - t_min) / (n - 1) * i
    x = f(t)
    file_out.write("{}, {}\n".format(t, x))

file_out.close()
