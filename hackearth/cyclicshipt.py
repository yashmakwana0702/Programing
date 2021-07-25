def main():
    t = int(input())
    while t > 0:
        count = 0
        i = 0
        n, k = map(int, input().split())
        a = input()
        b = rotate(a)
        x = binaryToDecimal(a)
        while i <k:
            if x == binaryToDecimal(b):
                i += 1
                if i == k:
                    print(count)
            count += 1
            b = rotate(b)
        t -= 1


def rotate(l):
    return l[-1:] + l[:-1]


def binaryToDecimal(n):
    return int(n, 2)


if __name__ == '__main__':
    main()
