def main() :
    outfile = open('data.txt', 'w')

    fname = input("Indtast uddannelse")

    outfile.write(fname + '\n')

    outfile.close
main()