__author__ = 'Vishal'

import sys

def runprogram():
    # test_cases = open(sys.argv[1], 'r')
    test_cases = open("mod.txt", 'r')


    for test in test_cases:
        list = test.split(',');

        print int(list[0])%int(list[1]);

    test_cases.close()

def main():
    runprogram()


main()