import sys

def runprogram():
    # test_cases = open(sys.argv[1], 'r')
    # test_cases = open("uniqueelements.txt", 'r')

    n = int(sys.stdin.readline().rstrip('\n'));

    i = 2
    sum = 0 ;
    count = 0 ;
    while True:
        k = 0
        for j in range(1, i,1):
            k += j
        sum += k
        count += 1 ;
        if  sum == n:
            print count ;
            break;
        elif sum > n:
            print count - 1;
            break;
        i = i + 1

def main():
    runprogram()


main()