
##############################
def f1 ( a, b, c ):
    return a+b*c

x1 = f1 ( 2, 3, 4 )
print ( f"x1={x1}" )

##############################
def f2 ( a, b, c=10 ):
    return a+b*c

x1 = f2 ( 2, 3 )
print ( f"x1={x1}" )

##############################
def f3 ( *a ):
    t = 0
    for x in a:
        t = t + x
    return t

x1 = f3 ( 2, 3, 4, 5 )
print ( f"x1={x1}" )


##############################
def insulation ( w=15, l=47, q=15 ):
    tw_f=9
    tw_i=6
    tl=16
    sq_in = ( tw_f*12 + tw_i ) * ( tl * 12 )
    print ( f"sq in for studio {sq_in}" )

    sq_in_pack = w * l * q
    packs = sq_in / sq_in_pack
    return packs

ii = insulation ( )
print ( f"packs needed {ii}" )


##############################

# Accessing a global value - a "Non-Pure" fucntion with side effects

a = 4
b = 2

def hard_to_test ( ) :
    global a, b
    a = ( a + 2 ) % 5
    return b + a


x1 = hard_to_test() 
print ( f"hard_to_test = {x1} first run" )

x1 = hard_to_test() 
print ( f"hard_to_test = {x1} 2nd run " )

x1 = hard_to_test() 
print ( f"hard_to_test = {x1} third run" )

x1 = hard_to_test() 
print ( f"hard_to_test = {x1} forth run" )

x1 = hard_to_test() 
print ( f"hard_to_test = {x1} fifth run" )

x1 = hard_to_test() 
print ( f"hard_to_test = {x1} sixth run" )

x1 = hard_to_test() 
print ( f"hard_to_test = {x1} seventh run" )

