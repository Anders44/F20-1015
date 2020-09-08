import csv

with open('new-top-firstNames.csv', 'r') as read_ref:
    csv_reader = csv.reader(read_ref)

    first = list(map(tuple, csv_reader))

    # print(first)

    with open('new-top-surnames.csv', 'r') as read_ref:
        csv_reader = csv.reader(read_ref)

        sir = list(map(tuple, csv_reader))

        # print(sir)

        first = first[1:]
        sir = sir[1:]

        g = 99
        for f in first:
            n = 55
            for l in sir:
                # ph = "303-111-1212"
                ph = "303-{:03d}-{:04d}".format(g,n)
                print ( f"{f[1]} {l[1].title()},{ph}" )
                n = n + 1
            g = g + 1
