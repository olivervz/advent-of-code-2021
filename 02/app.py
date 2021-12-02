def main():
    a = []
    with open('in.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            a.append(line.strip('\n'))
        
    forward = 0
    down = 0
    aim = 0
    for command in a:
        if 'forward' in command:
            val = int(command[command.find(' '):])
            forward += val
            down += aim * val
        if 'down' in command:
            aim += int(command[command.find(' '):])
        if 'up' in command:
            aim -= int(command[command.find(' '):])
    print(forward * down)

if __name__ == '__main__':
    main()