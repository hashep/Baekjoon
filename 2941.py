croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

text = input()

for c in croatian:
    text = text.replace(c, "*")  

print(len(text))