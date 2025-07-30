from collections import Counter

word = input().upper()  
counter = Counter(word) 

max_freq = max(counter.values()) 
most_common = [k for k, v in counter.items() if v == max_freq] 

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])