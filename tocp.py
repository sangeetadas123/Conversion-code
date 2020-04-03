
# Input:    .nt file with metadata
# Output:   .nt file in form of companion property


if __name__ == "__main__":

    filename1 = 'inst-SP.nt'
    filename2 = 'output_companion.nt'

    print("Reading file...")
    file1 = open(filename1, 'r', buffering=90000)
    file2 = open(filename2, 'w', buffering=90000)
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

            p11 = p1 + "." + str(cnt-9999) + "> "
            p12 = p1 + "." + str(cnt-9999) + ".SID> "

            file2.write(s1 + " " + p11 + o1 + " .\n")
            file2.write(s1 + " " + p12 + "<http://example.org#id_"+str(cnt) + "> " + " .\n")
            file2.write("<http://example.org#id_"+str(cnt) + "> " + mp1 + " " + o2 + " .\n")
            file2.write(p12 + "<http://www.w3.org/1999/02/22-rdf-syntax-ns#idPropertyOf> " + p11 + " .\n")
            file2.write(p11 + "<http://www.w3.org/1999/02/22-rdf-syntax-ns#companionPropertyOf> " + p1 + "> " + " .\n")
            
            
            

        i = (i + 1) % 3
        cnt = cnt + 1
    print("Done.")

    file1.close()
    file2.close()

    print("File saved.")

