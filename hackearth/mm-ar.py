def main():
    n, m = map(int, input().split())
    arr = []
    count = 0
    for i in range(n):
        a = [m]
        a = list(map(int, input().split()))
        arr.append(a)
    for i in range(m):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()


if __name__ == "__main__":
    main()
