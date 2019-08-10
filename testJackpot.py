def testJackpot(x):
	y = []
	for i in range(len(x)-1):
		if x[i] == x[i+1]:
			y.append(True)
		else:
			y.append(False)
	if False in y:
		return False
	else:
		return True

print(testJackpot(["&&&&","&&&&","&&&&","&&&&"]))
