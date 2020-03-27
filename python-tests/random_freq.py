import random
count_one = count_two = count_three = count_four = count_five = count_six = 0
random.seed()
for i in range (1,101):
    r = int(random.uniform(1,7))    
    if r == 1:
        count_one += 1
    if r == 2:
        count_two += 1
    if r == 3:
        count_three += 1
    if r == 4:
        count_four += 1
    if r == 5:
        count_five += 1
    if r == 6:
        count_six += 1

print("Freq one : ", count_one)
print("Freq two : ", count_two)
print("Freq three : ", count_three)
print("Freq four : ", count_four)
print("Freq five : ", count_five)
print("Freq six : ", count_six)
