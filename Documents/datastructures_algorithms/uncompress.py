def uncompress(s):
  number="0123456789"
  i=0
  j=0
  result=[]
  while j < len(s):
    if s[j] in number:
      j+=1
    else:
      result.append(int(s[i:j]) * s[j])
      j+=1
      i=j
  return ''.join(result)




uncompress("3n12e2z")