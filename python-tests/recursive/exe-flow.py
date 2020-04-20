def funtwo():
    print("this is fun two")
    return

def funone():
    funtwo()
    print("this is fun one")
    return

funone()