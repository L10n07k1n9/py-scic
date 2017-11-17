# Problemas

# Crear un programa que lea cada línea de un archivo e indique cuánto mide cada línea.


def read_each_line_length(s_file_path):
    result = []
    try:
        file, index = None, 0
        try:
            file = open(s_file_path, "r")
            index = 1
            result.append("File: {}".format(s_file_path))
            for line in file:
                result.append({"line": index, "length": len(line)})
                index = index + 1
        except IOError as ioerr:
            print("File doesn't exist" + ioerr.filename)
            result.append(-1)
        else:
            result.append(-2)
        finally:
            file.close()
            result.append(index)
    finally:
        return result


s_file_path = input("Please enter a file full or realtive path: ")
r1 = read_each_line_length(s_file_path)
print(r1[0])
if len(r1) > 2 and r1[-1] >= 0:
    # S = r1[slice(1, -1)]
    for line_info in r1[1:-1]:
        print(
            "Line: {} -> Length: {}".format(line_info["line"], line_info["length"]))
# Crear un programa que almacene los primeros 20 números de la sucesión de Fibonacci en formato csv.


def fibonacci(x):
    r, n, = [], 0
    if x < 0:
        return r
    while n < x:
        nl1 = n
        if n == 0:
            r.append(0)
        elif n <= 2:
            r.append(1)
        else:
            r.append(r[-1] + r[-2])
        n = n + 1
    return r


fibo_lst20 = fibonacci(20)
f = None
try:
    f, i = open("prob3.fibo20_seq.py.csv", "w"), 0
    f.write("index,fibonacci_computed\n")
    for n in fibo_lst20:
        f.write("{},{}\n".format(i, n))
        i = i + 1
finally:
    if f is not None:
        f.close()
