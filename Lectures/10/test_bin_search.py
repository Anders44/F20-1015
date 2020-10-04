"""
Test for binary search.
@author Philip  Schlump
"""

import csv

look_for = "Philip Schlump"

# binary_search performs a recursive binary search through a list of
# tuples where the [0] in the tuple is the "key" - looking for the 
# value passed in 'look_for'.  In this case the name.
# It will return a tuple of ("","") when not found.
def binary_search ( list_of_tuples, look_for ):
    if len(list_of_tuples) < 1:
        return ("","")
    if len(list_of_tuples) == 1 and list_of_tuples[0][0] == look_for:
        # print ( f"found with length 1, {list_of_tuples}" )
        return list_of_tuples[0]
    if len(list_of_tuples) == 1 :
        return ("","")
    mid = len(list_of_tuples) // 2
    # print ( f"mid = {mid} for {list_of_tuples}" )
    if list_of_tuples[mid][0] == look_for:
        # print ( f"found at mid={mid}, {list_of_tuples}" )
        return list_of_tuples[mid]
    if look_for < list_of_tuples[mid][0]:
        # print ( f"less than {look_for} passing {list_of_tuples[0:mid]}" )
        return binary_search ( list_of_tuples[0:mid], look_for )
    if look_for > list_of_tuples[mid][0] and (mid+1) < len(list_of_tuples):
        # print ( f"greater than {look_for} passing {list_of_tuples[mid:]}" )
        return binary_search ( list_of_tuples[mid+1:], look_for )
    return ("","")


# Automated Test - Of binary_search

n_err = 0
expect = ("","")
got = binary_search ( [], "x" )
if got != expect:
    print ( f"FAIL expected {expect} got {got}" )
    n_err = n_err + 1

expect = ("","")
got = binary_search ( [ ("Alice","123-123-1234" ) ], "x" )
if got != expect:
    print ( f"FAIL expected {expect} got {got}" )
    n_err = n_err + 1

expect = ("Alice","123-123-1234")
got = binary_search ( [ ("Alice","123-123-1234" ) ], "Alice" )
if got != expect:
    print ( f"FAIL expected {expect}2 got {got}" )
    n_err = n_err + 1

expect = ("Alice","123-123-1234")
got = binary_search ( [ ("Alice","123-123-1234" ), ( "Bob", "222-222-2222" ) ], "Alice" )
if got != expect:
    print ( f"FAIL expected {expect}2 got {got}" )
    n_err = n_err + 1

expect = ("Bob","222-222-2222")
got = binary_search ( [ ("Alice","123-123-1234" ), ( "Bob", "222-222-2222" ) ], "Bob" )
if got != expect:
    print ( f"FAIL expected {expect} got {got}" )
    n_err = n_err + 1

expect = ("","")
got = binary_search ( [ ("Alice","123-123-1234" ), ( "Bob", "222-222-2222" ) ], "Charlie" )
if got != expect:
    print ( f"FAIL expected {expect} got {got}" )
    n_err = n_err + 1

expect = ("","")
got = binary_search ( [ ("Alice","123-123-1234" ), ( "Bob", "222-222-2222" ),
( "Camile", "333-333-3333" ) ], "aaaa" )
if got != expect:
    print ( f"FAIL expected {expect} got {got}" )
    n_err = n_err + 1

expect = ("","")
got = binary_search ( [ ("Alice","123-123-1234" ), ( "Bob", "222-222-2222" ),
( "Camile", "333-333-3333" ) ], "Zed" )
if got != expect:
    print ( f"FAIL expected {expect} got {got}" )
    n_err = n_err + 1

expect = ( "Camile", "333-333-3333" )
got = binary_search ( [ ("Alice","123-123-1234" ), ( "Bob", "222-222-2222" ),
( "Camile", "333-333-3333" ) ], "Camile" )
if got != expect:
    print ( f"FAIL expected {expect} got {got}" )
    n_err = n_err + 1

if n_err == 0 :
    print ( "PASS" )
else:
    print ( f"{n_err} test(s) FAILED!" )

