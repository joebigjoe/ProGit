import os
import re

def ifISAndroid(str):
    firstToken = str[0:10]
    low = re.search(r"[a-z]", firstToken)
    num = re.search(r"[0-9]", firstToken)
    if (low != None or num !=None) and "-" not in firstToken:
        return True
    else:
        return False


def ifIsIOS(str):
    firstToken = str[0:10]
    if "-" in firstToken:
        return True
    else:
        return False


def ifIsNormal(str):
    return not (ifISAndroid(str) or ifIsIOS(str))


fileToAnalyze = os.getcwd() + "\\DBAll.csv"

# loop the lines
lines = []

# read file to list
with(open(file=fileToAnalyze, mode="r")) as filehandler:
    lines = filehandler.readlines()

# process list
for line in lines:
    loopcounter = 0
    currenttoken = line.split(',')[0].strip()
    if(ifIsNormal(line)):
        for line_ in lines:
            if currenttoken in line_:
                loopcounter = loopcounter + 1
    if loopcounter == 1:
        print(currenttoken)
