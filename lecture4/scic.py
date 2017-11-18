def open_csv_metadata(s_file_path):
    result = {}
    try:
        file, i = None, 1
        try:
            file = open(s_file_path, "r")
            data = {}
            data["rows"] = []
            for line in file:
                line_csv = line.replace("\n", "").split(",")
                if i == 1:
                    data["header"] = line_csv
                else:
                    data["rows"].append(dict(zip(data["header"], line_csv)))
                i = i + 1
            result["data"] = data
        except IOError as ioerr:
            print("File doesn't exist" + ioerr.filename)
            result["status"] = ioerr
        else:
            result["status"] = 0
        finally:
            file.close()
            result["file"] = s_file_path
            result["lines"] = i
    finally:
        return result


def load_matrix_csv(filename):
    f = open(filename, "r")
    mat = []
    for line in f:
        srow = line.split(",")
        row = list(map(lambda s: float(s), srow))
        mat.append(row)
    f.close()
    return mat


def save_matrix_csv(filename, mat):
    f = open(filename, "w")
    for row in mat:
        srow = list(map(lambda x: str(x), row))
        line = ", ".join(srow)
        f.write(line + "\n")
    f.close()


def get_line(filename, i):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines[i - 1]


def count_word(filename, word):
    f = open(filename)
    count = 0
    for line in f:
        words = line.split(" ")
        for w in words:
            if w.lower() == word.lower():
                count += 1
    return count
