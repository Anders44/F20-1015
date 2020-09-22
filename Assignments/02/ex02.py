v = 5
w = 3
r = v + w
print ( "v plus w = {}".format(r) )
if r != 8:
        print ( "FAILED - v+w incorrect result, expected 8 got", r )
        
v, w = 4, 2
print ( "v times w = {}".format(v * w ) )

v = 16
print ( "v integer devided by w = {}".format(v // w) )
print ( "v float devided by w = {}".format ( v / w ) )

w = 8
print ( "v minus w = {}".format( v - w ) )

v, w = 17, 9
print ( "remainder from v devided by w = {}".format( v % w ) )
