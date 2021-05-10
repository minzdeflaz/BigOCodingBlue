'''Suffix Structures
Bizon the Champion isn't just a bison. He also is a favorite of the "Bizons" team.

At a competition the "Bizons" got the following problem: "You are given two distinct words (strings of English letters), ss and tt. You need to transform word ss into word tt". The task looked simple to the guys because they know the suffix data structures well. Bizon Senior loves suffix automaton. By applying it once to a string, he can remove from this string any single character. Bizon Middle knows suffix array well. By applying it once to a string, he can swap any two characters of this string. The guys do not know anything about the suffix tree, but it can help them do much more.

Bizon the Champion wonders whether the "Bizons" can solve the problem. Perhaps, the solution do not require both data structures. Find out whether the guys can solve the problem and if they can, how do they do it? Can they solve it either only with use of suffix automaton or only with use of suffix array or they need both structures? Note that any structure may be used an unlimited number of times, the structures may be used in any order.

Dữ liệu nhập
The first line contains a non-empty word ss. The second line contains a non-empty word tt. Words ss and tt are different. Each word consists only of lowercase English letters. Each word contains at most 100 letters.

Dữ liệu xuất
In the single line print the answer to the problem. Print "need tree" (without the quotes) if word ss cannot be transformed into word tt even with use of both suffix array and suffix automaton. Print "automaton" (without the quotes) if you need only the suffix automaton to solve the problem. Print "array" (without the quotes) if you need only the suffix array to solve the problem. Print "both" (without the quotes), if you need both data structures to solve the problem.

It's guaranteed that if you can solve the problem only with use of suffix array, then it is impossible to solve it only with use of suffix automaton. This is also true for suffix automaton.
'''

def solve (inp1, inp2):
  i, j = 0, 0
  while len(inp1) != i and len(inp1) != j:
    if inp1[j] != inp2[i]:
      j += 1
    i += 1
    j += 1
  else:
    return (True, False)
  
  ar = False
  cou1, cou2 = {}, {}
  for i in inp1:
    if i not in cou1:
      cou1[i] = 1
    else:
      cou1[i] +=1
  for i in inp2:
    if i not in cou2:
      cou2[i] = 1 
    else:
      cou2[i] +=1
  for i in cou2:
    if i in cou1:
      if cou2[i] <= cou2[i]:
        ar = True
        continue
    ar = False
    break
  if ar == True:
    if len(inp1) > len(inp2):
      return (True, True)
    else:
      return (False, True)
  return (False,False)
inp1, inp2 = input(), input()
au, ar = solve(inp1, inp2)
if au == True:
  if ar == True:
    print("both")
  else:
    print("automaton")
else:
  if ar == True:
    print("array")
  else:
    print("need tree")