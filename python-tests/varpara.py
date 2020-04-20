varpara(normal="nor para",varpara_tuple=())
varpara(1,(2,3))

def varpara(normal, varpara_tuple):
    print("This is normal para : ", normal)
    for varpara in varpara_tuple:
        print(varpara)
    return