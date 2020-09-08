import csv

look_for = "Philip Schlump"

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

    for rr in list_of_tuples:
        if rr[0] == look_for:
            print ( f"found {look_for} with phone number {rr[1]}" )

