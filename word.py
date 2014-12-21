import sys

def runprogram():
    # test_cases = open(sys.argv[1], 'r')
    # test_cases = open("uniqueelements.txt", 'r')

    word = sys.stdin.readline().rstrip('\n');
    k = 0;
    for w in word:
        if w.isupper():
            k= k+1

    if k > int(len(word) / 2) :
        word = word.upper();
        print word
    else:
        word = word.lower()
        print word

def main():
    runprogram()


main()