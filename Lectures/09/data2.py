want = 'tom'
di = { 'bob':18, 'jane':19, 'tom':16 }
if want in di:
    age = di[want]
    print ( f"Found: {want} age {age}" )
else:
    print ( f"not found {want}" )

