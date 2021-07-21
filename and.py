
def main():
    t = int(input())
    while(t > 0):
        n = int(input())
        a = []
        for i in range(0, n):
            a.append(int(input()))
        cout = 0
        for i in range(0, n):
            for j in range(i, n):
                if(a[i] & a[j] >= a[i] ^ a[j]):
                    cout = cout+1
                break
    print(cout)
    t = t-1


if __name__ == '__main__':
    main()
