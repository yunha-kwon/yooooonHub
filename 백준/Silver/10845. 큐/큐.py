import sys

N = int(sys.stdin.readline())
my_queue = []

for i in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        my_queue.insert(0, command[1])

    elif command[0] == 'pop':
        if len(my_queue) == 0:
            print(-1)
        else:
            print(my_queue.pop())

    elif command[0] == 'size':
        print(len(my_queue))

    elif command[0] == 'empty':
        if len(my_queue) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(my_queue) == 0:
            print(-1)
        else:
            print(my_queue[len(my_queue)-1])

    elif command[0] == 'back':
        if len(my_queue) == 0:
            print(-1)
        else:
            print(my_queue[0])