import numpy as np


def printLinSpace(a):
	s = ""
	for i in a:
		s += str(i) + ','

	print s

printLinSpace(np.linspace(-120,120,31))

printLinSpace(np.linspace(3,7,3))

printLinSpace(np.linspace(0,2 * np.pi, 19))