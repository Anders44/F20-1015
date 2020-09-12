
# ex1 takes the numeric parameter 'n' and it is less than 11
# adds 2, otherwise it returns 55.
def ex1 ( n ):
    if n <= 10:
        return n+2
    else:
        return 55

# Automated Test - Version 1

x = ex1 ( -1 )
if x != 1:
    print ( "FAIL" )

x = ex1 ( 1 )
if x != 3:
    print ( "FAIL" )


x = ex1 ( 10 )
if x != 12:
    print ( "FAIL" )


x = ex1 ( 20 )
if x != 55:
    print ( "FAIL" )


print ( "PASS" )
