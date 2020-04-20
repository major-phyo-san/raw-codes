try:
    fh = open("test.txt","w")
    try:
        fh.write("this is a test file")
    finally:
        fh.close()
except IOError as ioerror:
    print("IO Error")
    print(str(IOError))
except OSError as generror:
    print(str(generror))