def main():
    t = int(input())
    while t > 0:
        t -= 1
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        while n < k:
            k = k-n
        arr = rotate(arr, k)
        print(*arr, sep=" ", end="\n")


def rotate(l, n):
    return l[-n:] + l[:-n]


if __name__ == '__main__':
    main()
