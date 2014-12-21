import sys

def runprogram():

    # sys.stdin  = open("CF266B.txt")
    f = sys.stdin;

    line = f.readline().rstrip('\n');
    k = line.split(" ");
    n = int(k[0]);
    t = int(k[1]);

    line = f.readline().rstrip('\n');

    for i in range(0,t):
        k = 0;
        newline = ""
        while k < n :
            if  k < n- 1 :
                if  line[k] == 'B' and line[k+1] == 'G':
                    newline += line[k+1] ;
                    newline += line[k] ;
                    k += 2;
                else:
                    newline += line[k];
                    k += 1
            else:
                newline += line[k];
                k += 1
        line = newline;
    print line;

def main():
    runprogram()


main()
