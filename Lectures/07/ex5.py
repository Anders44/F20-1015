
# ex1 takes the numeric parameter 'n' and it is less than 11
# adds 2, otherwise it returns 55.
def ex1 ( n ):
    # return -55555 # Uncomment to test automated test code.  All tests will fail.
    if n <= 10:
        return n+2
    else:
        return 55

# Automated Test - Version 2

n_err = 0
x = ex1 ( -1 )
if x != 1:
    print ( f"FAIL expected 1 got {x}" )
    n_err = n_err + 1

x = ex1 ( 1 )
if x != 3:
    print ( f"FAIL expected 3 got {x}" )
    n_err = n_err + 1


x = ex1 ( 10 )
if x != 12:
    print ( f"FAIL expected 12 got {x}" )
    n_err = n_err + 1


x = ex1 ( 20 )
if x != 55:
    print ( f"FAIL expected 55 got {x}" )
    n_err = n_err + 1


if n_err == 0 :
    print ( "PASS" )
else:
    print ( f"{n_err} test(s) FAILED!" )
