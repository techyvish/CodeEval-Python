__author__ = 'Vishal'

import sys

def runprogram():
    # test_cases = open(sys.argv[1], 'r')
    test_cases = open("wordtodigit.txt", 'r')

    numbers = { "zero":"0",
                "one":"1",
                "two":"2",
                "three":"3",
                "four":"4",
                "five":"5",
                "six":"6",
                "seven":"7",
                "eight":"8",
                "nine":"9", }



    string =  ""
    for test in test_cases:
        list = test.rstrip('\n').split(';')
        for number in list:
            string += numbers[number]
        print string
        string = ""

    test_cases.close()

def main():
    runprogram()


main()
