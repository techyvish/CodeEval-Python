import sys

def runprogram():
    test_cases = open(sys.argv[1], 'r')
    # test_cases = open("reversewords.txt", 'r')


    for test in test_cases:
        list = test.rstrip('\n').split(" ")
        i = 0
        string = ""
        list.reverse()
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
