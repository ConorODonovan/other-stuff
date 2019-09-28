import time

def fibonacci_sequence(a, b):
	c = a + b
	print("{}".format(c))
	time.sleep(0.1)
	fibonacci_sequence(b, c)

if __name__ == "__main__":
	a = 0
	b = 1

	print("{}".format(a))
	print("{}".format(b))

	fibonacci_sequence(a, b)
