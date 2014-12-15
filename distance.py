__author__ = 'Vishal'

import sys
import math

def runprogram():
    test_cases = open(sys.argv[1], 'r')
    # test_cases = open("distance.txt", 'r')

    for test in test_cases:
        list = test.rstrip('\n').split(" ")
        x1 = int(list[0].lstrip('(').rstrip(','));
        y1 = int(list[1].rstrip(')'));
        x2 = int(list[2].lstrip('(').rstrip(','));
        y2 = int(list[3].rstrip(')'));

        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2);
        print int(distance);

    test_cases.close()

def main():
    runprogram()


main()