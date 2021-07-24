def main():
    t = int(input())
    ins = [2]
    color=[]
    while(t > 0):
        ins = input().split()
        color=input().split()
        n = int(ins[0])
        k = int(ins[1])
        print(n, k, color)
        
        t -= 1



if __name__ == "__main__":
    main()
