import sys, getopt

inputfile=''
outputfile=''
buffile=''
try:
    opts, args = getopt.getopt(sys.argv[1:],"hupi:o:",["ifile=","ofile=","buffile="])
except getopt.GetoptError:
    print('exception help test.py -i <inputfile> -o <outputfile>')
    sys.exit(2)

for opt, arg in opts:
    if opt=="-h":
        print('normal help test.py -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg
    elif opt !="--buffile":
        print("No buffile")
print("Input file is", inputfile)
print("Output file is", outputfile)
print("Buffer file is",buffile)