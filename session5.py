from math import sin
from math import pi
from pip import main
from tabulate import tabulate

def func(x):
    return sin(x)

if __name__ == "__main__":
    topNum = 1000
    mainList = []
    for i in range(topNum+1):
        val = (i/topNum) * 2*pi
        mainList.append([i, val, func(val)])
    print(tabulate(mainList, headers=["index", "value", "sin(x)"]))