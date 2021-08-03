n, m = map(int, input().split())
arr = []
for i in range(n):
    a = list(input())
    arr.append(a)
c = 0
print(arr)
# horizontal
for i in range(n):
    for j in range(m):
        if m-j >= 4:
            # print(m,j,i)
            if arr[i][j] == 's' and arr[i][j+1] == 'a' and arr[i][j+2] == 'b' and arr[i][j+3] == 'a':
                # print("yes")
                c += 1
# vertical
for i in range(m):
    for j in range(n):
        if n-j >= 4:
            # print(m,j,i)
            if arr[j][i] == 's' and arr[j+1][i] == 'a' and arr[j+2][i] == 'b' and arr[j+3][i] == 'a':
                # print("yes")
                c += 1
# diagonal
for i in range(n-4):
    for j in range(m-4):
        if n-i >= 4 and m-j >= 4:
            # print(m,j,i)
            if arr[i][j] == 's' and arr[i+1][j+1] == 'a' and arr[i+2][j+2] == 'b' and arr[i+3][j+3] == 'a':
                # print("yes")
                c += 1

print(c)
