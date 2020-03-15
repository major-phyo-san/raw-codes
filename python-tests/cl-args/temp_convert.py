import sys, getopt

primary = ''
target = ''
value = 0.0

aggresive_convert = True

try:
    opts,args = getopt.getopt(sys.argv[1:],"arh",["primary=","target=","value=","help"])
except getopt.GetoptError:
    print("Invalid use of parameters. Type -h or --help to get help")
    sys.exit(2)

if not opts:
    print("No parameter input. Type -h or --help to get help")
    sys.exit(2)

for opt, arg in opts:
    if opt == "-h" or opt == "--help":
        print("Usage of parameter text")
        sys.exit()
    elif opt == "-a":
        aggresive_convert = True
    elif opt == "-r":
        aggresive_convert = False
    elif opt == "--primary":
        primary = arg
    elif opt == "--target":
        target = arg
    elif opt == "--value":
        value = float(arg)

if primary == 'C':
    if target == 'F':
        result = (9/5) * (value + 32)
        if not aggresive_convert:
            result = int(result)
        print("Equivalent fahrenheit = ", result)

    elif target == 'K':
        result = value + 273
        print("Equivalent kelvin = ", result)

elif primary == 'F':
    if target == 'C':
        result = (5/9) * (value - 32)
        if not aggresive_convert:
            result = int(result)
        print("Equivalent celsius = ", result)

    elif target == 'K':
        result = ((5/9) * (value - 32) ) + 273
        print("Equivalent kelvin = ", result)
