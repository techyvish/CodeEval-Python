___author__ = 'Vishal'

import sys
import re

from swampy.TurmiteWorld import *

def runprogram():
    # test_cases = open(sys.argv[1], 'r')
    test_cases = open("capitalize.txt", 'r')


    for test in test_cases:
        list = test.split(" ");
        i = 0
        string = ""
        for word in list:
            if i != 0:
                string += " "
            string += word
            i += 1
        print string
    test_cases.close()

def main():
    runprogram()


main()
