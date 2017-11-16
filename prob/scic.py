def Load_Matrix_CSV(filename, mode="r", separator=","):
    file, mat = open(filename, mode), []
    for line in file:
        mat.append(list(map(lambda s: float(s), line.split(separator))))
    file.close()
    return mat


def Save_Matrix_CSV(filename, mat):
    file = open(filename, "w")
    for m in mat:
       line = list(map(lamda x: str(x), m)))
       file.write("{} \n", line)
    file.close()
