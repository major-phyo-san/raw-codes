count = 0
find_this = 'Terry'
names = ['Charles','Boyle','Danny','Alex']
if find_this in names:
    for name in names:
        if find_this == name:
            break
        count += 1
    print(find_this, 'found at ',count)
else:
    print(find_this, 'not found')