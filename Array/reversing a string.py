def reverse(string):
  mylist=[]
  for i in range(len(string)-1,-1,-1):
    mylist.append(string[i])
  return ''.join(mylist)

x=reverse('I am Walker')
print(x)

# or just string[::-1]