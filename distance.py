__author__ = 'Vishal'

import sys

def runprogram():
    # test_cases = open(sys.argv[1], 'r')
    test_cases = open("distance.txt", 'r')


    for test in test_cases:
        list = test.rstrip('\n').split(",")
        list.sort()
        s1 = set(list)
        print s1

    test_cases.close()

def main():
    runprogram()


main()