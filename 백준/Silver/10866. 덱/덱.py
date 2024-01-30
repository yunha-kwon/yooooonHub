import sys

N = int(sys.stdin.readline())
my_deque = []

for i in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        my_deque.insert(0, command[1])

    elif command[0] == 'push_back':
        my_deque.append(command[1])
    
    elif command[0] == 'pop_front':
        if len(my_deque) == 0:
            print(-1)
        else:
            print(my_deque.pop(0))
    
    elif command[0] == 'pop_back':
        if len(my_deque) == 0:
            print(-1)
        else:
            print(my_deque.pop())

    elif command[0] == 'size':
        print(len(my_deque))

    elif command[0] == 'empty':
        if len(my_deque) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(my_deque) == 0:
            print(-1)
        else:
            print(my_deque[0])

    elif command[0] == 'back':
        if len(my_deque) == 0:
            print(-1)
        else:
            print(my_deque[len(my_deque)-1])