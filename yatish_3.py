s=input()
p=''
for i in s:
  if i.isdigit()==True:
    p+=i
  elif i=="-":
    p+=i

a = int(p)
print(a)

