def raisefloat(num):
    if not isinstance(num,int):
        typenum = str(type(num))
        raise Exception(typenum)
    print(num)

try:
    raisefloat('a')
except Exception as error:
    print("except int but received ", str(error.args[0]))