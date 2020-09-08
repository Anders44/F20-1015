look_for = "Philip Schlump"

def binary_search ( list_of_tuples, look_for ):
    if len(list_of_tuples) < 1:
        return ("","")
    if len(list_of_tuples) == 1 and list_of_tuples[0][0] == look_for:
        return list_of_tuples[0]
    if len(list_of_tuples) == 1 :
        return ("","")
    mid = len(list_of_tuples) // 2
    if list_of_tuples[mid][0] == look_for:
        return list_of_tuples[mid]
    if look_for < list_of_tuples[mid][0]:
        return binary_search ( list_of_tuples[0:mid], look_for )
    if look_for > list_of_tuples[mid][0]:
        return binary_search ( list_of_tuples[mid:], look_for )
    return ("","")

list_of_tuples = [ ("Philip Schlump", "720-209-7888"),
("Marry Spender", "011-221-411-821"), ("Adam Savage", "303-444-1212"),
("John Dijkstra", "000-000-0000"), ("Abra Cadabra", "000-000-0000") ]

list_of_tuples.sort()

found_result = binary_search ( list_of_tuples, look_for )
if found_result[0] == "":
    print ( f"{look_for} not found" )
else:
    print ( f"found {look_for} with phone number {found_result[1]}" )
