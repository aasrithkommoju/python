k = input()
r = ""
if k[0]=="-":
    r+="-"
for i in k:
    if i.isdigit():
        r+=i
print(r)
print(type(r))
