def testJackpot(x):
	# y = []
	# for i in range(len(x)-1):
	# 	if x[i] == x[i+1]:
	# 		y.append(True)
	# 	else:
	# 		y.append(False)
	# if False in y:
	# 	return False
	# else:
	# 	return True
	return True if len(list(set(x))) == 1 else False
	

	# return [a for a,i in range(len(x)) if x[i] == x[i]+1]

print(testJackpot(["&&&&","&&&&","&&&&","&&&&"]))