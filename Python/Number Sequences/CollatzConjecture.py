import time

def collatz(num, steps):
	if num > 1:
		if num % 2 == 0:
			num = num/2
		else:
			num = (3 * num) + 1
		# time.sleep(0.25)
		print("{}".format(int(num)))
		collatz(num, steps + 1)
	else:
		print("Steps: {}".format(steps))


if __name__ == "__main__":
	start = input("Please enter a number: ")
	start_int = int(start)
	steps = 0

	collatz(start_int, steps)
