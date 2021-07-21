def main():
    t = int(input())

    for ii in range(t):
        # a = []
        n = int(input())

        a = list(map(int, input().split()))
        # for j in range(n):
        #     x = int(input())
        #     a.append(x)

        i = 0
        j = n-1

        le = 0
        ri = 0

        c1 = 0
        c2 = 0

        while i < j:

            if le == ri:
                le = le+a[i]
                ri = ri+a[j]
                c1 += 1
                c2 += 1
                i += 1
                j -= 1

            elif le > ri:
                c1 = c1+1
                ri = ri + a[j]
                j = j-1

            else:
                c2 = c2+1
                le = le + a[i]
                i = i+1

        if n % 2 == 1:
            if le <= ri:
                c1 += 1

            else:
                c2 += 1

        print(c1, c2)


if __name__ == '__main__':
    main()
