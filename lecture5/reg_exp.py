import re


def match():
    pattern = '[\w\.\-_]+@\w+(\.\w{2,4}){1,3}'
    text = "mi correo es leo@gmail.com y el otro es l2@info.co.jp"
    for m in re.finditer(pattern, text):
        print("{} starts in {} to {}".format(m.group(
            0), m.start(), m.start() + len(m.group(0))))


match()
