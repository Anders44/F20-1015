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

# open file in read mode
with open('phone-book.csv', 'r') as read_ref:
    # csv.reader() takes a file_ref as an input.
    # This is a chunk of data that associates the name/mode
    # with the actual file on the system and allows reading
    # and writing of the file.
    csv_reader = csv.reader(read_ref)

    # Get all rows of csv from csv_reader object as list of tuples
    list_of_tuples = list(map(tuple, csv_reader))

    # display all rows of csv
    # print(list_of_tuples)

    # pre-process the list - sort it.
    list_of_tuples.sort()
    # print(list_of_tuples)

    found_result = binary_search ( list_of_tuples, look_for )
    if found_result[0] == "":
        print ( f"{look_for} not found" )
    else:
        print ( f"found {look_for} with phone number {found_result[1]}" )
