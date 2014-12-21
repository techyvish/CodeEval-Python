__author__ = 'Vishal'

import sys,math

def runprogram():

    sys.stdin  = open("CF489B.txt")
    f = sys.stdin;

    list = f.readline().rstrip('\n').split(" ");
    n = int(list[0]);
    m = int(list[1]);
    for i in range(0,n):
        for j in range(0,m):
            print i,j;


def main():
    runprogram()


main()
