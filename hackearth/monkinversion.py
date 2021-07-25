def main():
    t = int(input())
    while t > 0:
        n = int(input())
        arr = []
        count = 0
        for i in range(n):          # A for loop for row entries
            a = []     # A for loop for column entries
            a = list(map(int, input().split()))
            arr.append(a)
        for i in range(n):
            for j in range(n):
                for x in range(i, n):
                    for y in range(j, n):
                        if arr[i][j] > arr[x][y]:
                            count += 1
        print(count)
        t -= 1


if __name__ == '__main__':
    main()
