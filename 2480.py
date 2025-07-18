A, B, C = map(int, input().split())

if A == B == C:
    print(10000+A*1000)
elif A == B or B == C:
    print(1000+B*100)
elif C == A:
    print(1000+C*100)
    
if A != B and A != C and B != C:
    if A >= B and A >= C:
        print(A*100)
    if B >= A and B >= C:
        print(B*100)
    if C >= B and C >= A:
        print(C*100)