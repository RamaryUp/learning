"""
Test of yield usage used to create a generator.
"""

def iterfunc(x):
  print("[iterfunc] begin")
  for i in range(x):
    yield i
  for i in range(2 * x, 3 *x):
    yield i
  print("[iterfunc] end")
  
print("Start")
for i in (iterfunc(4)):
  print("iterfunc->"+str(i))
  
f = iterfunc(5)
print(next(f))
print(next(f))
print(next(f))
print(f.__next__()) # similar to next(f)
print(next(f))

print("End")

"""
Output :
Start
[iterfunc] begin
iterfunc->0
iterfunc->1
iterfunc->2
iterfunc->3
iterfunc->8
iterfunc->9
iterfunc->10
iterfunc->11
[iterfunc] end
[iterfunc] begin
0
1
2
3
4
End
"""