#json
import json
d ={1:12,2:'b'}
c =json.dumps(d,indent =12)
print(c)
f =json.loads(c)
print(type(f))


