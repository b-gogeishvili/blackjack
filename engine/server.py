import sys

for line in sys.stdin:
    command = line.strip()

    if command == "ping":
        print("pong")
    elif command == "quit":
        break
    else:
        print("unknown")

