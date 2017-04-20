import uuid, re

with open('newmovieActors.cql', 'r') as f:
    lines = f.readlines()
    
for line in lines:
    if line.find('VALUES') > -1:
        r = re.search('VALUES \([0-9]+, ', line)
        id = "VALUES ('%s', " % uuid.uuid1()
        t = line.replace(r.group(0), id)
        print(t.replace('(movieid,', '(uuid, ' ).strip())
    else:
        print(line.strip())
        