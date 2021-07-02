n = int(input())
if n < 26:
  print("NO")
  exit()
string = input()
string = string.lower()
exist = [chr(i) for i in range(97, 123)]
for i in string:
  if i in exist:
    exist.remove(i)
if len(exist) == 0:
  print("YES")
else:
  print("NO")