n = 0
def tri_recursion(k,n):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result,'',n)
    n+=1
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)