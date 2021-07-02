# Source: https://codeforces.com/problemset/problem/691/A

def isFasten (length, buttons):
  if length == "1":
    if buttons[0] == "0":
      return "NO"
    return "YES"
  count = 0
  for i in buttons:
    if i == "0":
      count += 1
      if count > 1:
      	return "NO"
  if count == 0:
    return "NO"
  return "YES"

if __name__ == "__main__":
  length = input()
  buttons = input().split()
  print(isFasten(length, buttons))