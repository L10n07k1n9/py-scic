import re


def match():
    # pattern = r".*(PH):+\s*([0-9]+)[\%.\n]*?(.*)"
    patternPH = r".*(PH):+\s*(?P<PH>[0-9]+)\%[\s\n]*"
    patternTEMP = r".*?(TEM).*?(?P<TEMP>[0-9]+)C[\s\n]+?"
    patternDIL = r".*?(DIL).*?(?P<DIL>[0-9]+)u[\s\n]*?"
    text = """* PH: 27%
            * TEMPERATURA: 120C
            * DILATACION: 5u"""
    m = re.match(patternPH + patternTEMP + patternDIL, text)
    # return m.groups()
    return m.groupdict()


print(match())
