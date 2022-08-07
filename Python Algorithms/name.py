import sys

if len(sys.argv) < 2:
    sys.exit("To few arguments👇️")

for arg in sys.argv[1:]:
	print("🍉️ Hello, my name is", arg)

