def functhree():
    print("3")

def functwo():
    functhree()
    print("2")

def funcone():
    functwo()
    print("1")


funcone()