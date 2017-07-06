import dboperation
import json

a = dboperation.query()
result = []
for row in a:
    b={}
    b['w'] = row[0]
    b['c'] = row[1]
    b['d'] = row[2]
    result.append(b)

re = json.dumps(result)


print(re)