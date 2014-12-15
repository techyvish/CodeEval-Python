__author__ = 'Vishal'

import sys

def runprogram():
    test_cases = open(sys.argv[1], 'r')
    # test_cases = open("authorname.txt", 'r')


    for test in test_cases:
        list = test.split("|");
        str1 = list[0];
        str2 = list[1].lstrip(' ').rstrip('\n');
        numberlist = str2.split(' ');
        str = "";

        for number in numberlist:
            str += str1[int(number)-1]

        print str;

    test_cases.close()

def main():
    runprogram()


main()
