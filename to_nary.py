
# Input:    .nt file with metadata
# Output:   .nt file in form of nary representation


if __name__ == "__main__":

    filename1 = 'inst-SP.nt'
    filename2 = 'output_nary1.nt'
    filename4 = 'output_nary2.nt'

    print("Reading file...")
    file1 = open(filename1, 'r', buffering=90000)
    file2 = open(filename2, 'w', buffering=90000)
    file4 = open(filename4, 'w', buffering=90000)

    print("Done.")

    i = 0  # used to keep track of current line
    cnt = 10000  # used to create unique-id

    print("Processing file...")
    s1 = p1 = o1 = mp1 = o2 = ""
    for line in file1.readlines():
        data = line.split(sep=' ')
        if i == 0:
            s1 = data[0]
            o1 = data[2]
        elif i == 1:
            p1 = data[2][:-1]
        elif i == 2:
            mp1 = data[1]
            o2 = data[2]

            uid1 = "<http://example.org#id_" + str(cnt) + ">"

            file2.write(s1 + " " + p1 + "-s> " + uid1 + " .\n")
            file2.write(uid1 + " " + p1 + "-v> " + o1 + " .\n")
            file2.write(uid1 + " " + mp1 + " " + o2 + " .\n")
            file2.write(p1 + "-s> " + "<http://example.org/statementProperty> " + p1 + "> " + " .\n")
            file2.write(p1 + "-v> " + "<http://example.org/valueProperty> " + p1 + "> " + " .\n")

            '''file3.write(s1 + " " + p1 + "-s> " + uid1 + " .\n")
            file3.write(uid1 + " " + p1 + "-v> " + o1 + " .\n")
            file3.write(uid1 + " " + mp1 + " " + o2 + " .\n")'''

            file4.write(s1 + " " + p1 + "> " + uid1 + " .\n")
            file4.write(uid1 + " " + p1 + "-value> " + o1 + " .\n")
            file4.write(uid1 + " " + mp1 + " " + o2 + " .\n")


        i = (i + 1) % 3
        cnt = cnt + 1
    print("Done.")

    file1.close()
    file2.close()
    file3.close()
    file4.close()

    print("File saved.")

