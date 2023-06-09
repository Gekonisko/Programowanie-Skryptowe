import argparse


def RemoveLeadingSpaces(line):
    i = 0
    while line[i] == " ":
        i += 1
    return line[i:]


def RemoveSpaces(line):
    result = ""
    charFlag = False
    for sign in line:
        if not charFlag and sign != " ":
            charFlag = True
        elif not charFlag:
            result = result + sign
        if charFlag and sign != " ":
            result = result + sign
    return result


def FormatLine(line, sign):
    line = (line.split(sign))[0]
    if args.leading_spaces:
        line = RemoveLeadingSpaces(line)
    if args.spaces:
        line = RemoveSpaces(line)
    return line


def FormatData(file_data):
    sign = '\\'
    if args.c:
        sign = args.c
    data = []
    for line in file_data:
        line = FormatLine(line, sign)
        data.append(line)
    return "".join(data)


def CheckCorrectnessOfPaths():
    while args.path == "":
        print("Specify file name")
        args.path = input().split()
        try:
            for fileName in args.path:
                open(fileName, "r")
        except:
            print("This file don't exist")
            args.path = ""


def RemoveLogicalLinesFromFiles():
    for file_name in args.path:
        with open(file_name) as f:
            lines = f.readlines()
            print(file_name)
            print(FormatData(lines))


parser = argparse.ArgumentParser(description='Conversion of logical lines to physical.')
parser.add_argument('-c', type=str, help="A continuation character for input files (default: '\\n')")
parser.add_argument('--leading-spaces', action="store_true", help="Deletes all of leading spaces")
parser.add_argument('--spaces', action="store_true", help="Deletes all spaces, without leading ones")
parser.add_argument('path', type=str, nargs='*', default="")

args = parser.parse_args()

if __name__ == '__main__':
    CheckCorrectnessOfPaths()
    RemoveLogicalLinesFromFiles()
