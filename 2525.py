A, B = map(int, input().split())
C = int(input())
D = 0

if(C > 60):
    D = C // 60
    C = C % 60

A = A + D
B = B + C

if (B > 59):
    B = B - 60
    A = A + 1

if(A > 23):
    A = A - 24

print(A, B)