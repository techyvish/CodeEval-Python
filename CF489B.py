import sys,math
from collections import Counter;
def runprogram():

    sys.stdin  = open("CF489B.txt")
    f = sys.stdin;

    n  = int(f.readline().rstrip('\n'));
    boyskills = f.readline().rstrip('\n').split(" ");

    m  = int(f.readline().rstrip('\n'));
    girlskills = f.readline().rstrip('\n').split(" ");

    boyskills.sort();
    girlskills.sort();

    for i in range(0,n):
        for j in range(0,m ):
            if math.fabs( int(boyskills[i]) - int(girlskills[j])) <=1:
                girlskills[j] = 1000;

    print girlskills.count(1000);


def main():
    runprogram()


main()
