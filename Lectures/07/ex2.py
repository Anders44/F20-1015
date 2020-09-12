
# ex1 takes the numeric parameter 'n' and it is less than 11
# adds 2, otherwise it returns 55.
def ex1 ( n ):
    if n <= 10:
        return n+2
    else:
        return 55

# Examples of runing ex1
x = ex1(5)
print ( f"x={x}" )

x = ex1(11)
print ( f"x={x}" )


