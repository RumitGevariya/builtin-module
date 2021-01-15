#rex
import re
strs ='my name is rumit.my email add is rumitpatel98@gmail.com and jay email id is jaypatel98@gmail.com. and remit nu is 9925881941 and jay mo num is 832306239123.'
pattern ='[a-z0-9]+[@]\w+[.]\w{2,3}'
pat2 ='\d{10}'
a =re.search(pat2,strs)
f =re.match(pattern,strs)
b =re.findall(pat2,strs)
# c =re.split(' ',strs)
d =re.sub(' ','rumit',strs)
e =re.compile(strs)
# print(a.group())
# print(a.span())
# print(a.string)
print(b)


