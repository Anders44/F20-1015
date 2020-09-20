
want = 'tom'
key = [ 'bob', 'jane', 'tom' ]
val = [ 18, 19, 16 ]

age = -1
ii = 0
while ( ii < len(key) ):
    if key[ii] == want :
        age = val[ii]
    ii = ii + 1

if age > 0:
    print ( f"Found: {want} age {age}" )
else:
    print ( f"not found {want}" )

