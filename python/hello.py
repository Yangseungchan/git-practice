import sys

def hello():
	print("hello world")

def welcome():
	print("welcome")

def main():
	if(sys.argv[1] == 'hello'):
		hello()
	else:
		welcome()

if __name__ == '__main__':
        main()
