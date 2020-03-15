a = 169
x = 3.0
count = 0
while True:
	y = (x + a/x) / 2
	count += 1
	if abs(y-x) < 0.00000001:
		print(y)
		print("total steps : ",count)
		break
	x = y
	