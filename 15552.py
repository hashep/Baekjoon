import sys

T = int(sys.stdin.readline()) 

result = []

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split()) 
    result.append(str(A + B))  

sys.stdout.write("\n".join(result) + "\n")