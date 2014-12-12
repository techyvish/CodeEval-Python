__author__ = 'Vishal'

import sys
import re

def runprogram():
    test_cases = open(sys.argv[1], 'r')
    # test_cases = open("setintersection.txt", 'r')

    for test in test_cases:
        lists = test.split(";");

        set1 = re.split(",|\\n",lists[0]);
        set2 = re.split(",|\\n",lists[1]);

        j = 0
        arr = []
        if set1[0] < set2[0]:
            for item in set1:
                if item == set2[j]:
                    if j < len(set2):
                        j += 1
                    arr.append(item)

        else:
            for item in set2:
                if item == set1[j]:
                    if j < len(set1):
                        j += 1
                    arr.append(item)

        i = 0
        string = ""
        for item in arr:
            if i != 0:
                string += ","
            string += item
            i += 1
        print string


    test_cases.close()


def main():
    runprogram()


main()
