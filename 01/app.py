def main():
    a = []
    with open('in.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            a.append(int(line.strip('\n')))
        
    incs = 0
    incs_2 = 0
    # part 1
    for i in range(1, len(a)):
        if a[i] > a[i-1]:
            incs += 1
    # part 2
    for i in range(3, len(a)):
        if a[i] + a[i-1] + a[i-2] > a[i-1] + a[i-2] + a[i-3]:
            incs_2 += 1
    print(incs, incs_2)

if __name__ == '__main__':
    main()