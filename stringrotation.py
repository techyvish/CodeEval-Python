__author__ = 'Vishal'

import sys

def runprogram():

    line = sys.stdin.readline()
    while line.rstrip('\n') != '0':
        print line,
        line = sys.stdin.readline()
    # test_cases = open(sys.argv[1], 'r')
    test_cases = open("wordtodigit.txt", 'r')

    string =  ""
    for test in test_cases:
        list = test.rstrip('\n').split(',')

    test_cases.close()

def main():
    runprogram()

main()
