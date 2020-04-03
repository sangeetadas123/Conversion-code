

file2 = open('wikidata-statements-dataset52.nt', 'w')
j=0
cnt = 10000  # used to create unique-id
with open('/home/sangeeta/d1/wikidata-statements-dataset41.nq', 'r') as f1:
    
    for line in f1:
        print(j)
        s = ""
        o = ""
        p = ""
        u = ""
        fs = 0
        fp = 2
        fo = 4
        fu = 6
        fl = 0
        f2 = 0
        for i in range(0, len(line)):
            if line[i] == '<' and fs == 0:
                fl = 1
                s = line[i]
                fs = 1
            elif line[i] == '>' and fs == 1:
                fl = 0
                s = s + line[i]
                fs = 2
            elif line[i] == '<' and fp == 2:
                fl = 1
                p = line[i]
                fp = 3

            elif line[i] == '>' and fp == 3:
                fl = 0
                p = p + line[i]
                fp = 5
            elif line[i] == '<' and fo == 4:
                fl = 1
                o = line[i]
                fo = 5
            elif line[i] == '_' and fo == 4:
                fl = 1
                o = line[i]
                fo = 5

            elif fo == 4 and line[i] == "\"":
                fl = 1
                o = line[i]
                fo = 5
            elif fo == 5 and line[i] == "<" and fu == 6 and line[i+1]=='h' and line[i+2] == 't':
                fl = 1
                u = line[i]
                fo = 6
                #print "done"

                fu = 7
            elif line[i] == '>' and fu == 7:
                fl = 0
                u = u + line[i]
                fu = 9
                #print "done1"

            elif fl == 1 and fs == 1:
                s = s + line[i]
            elif fl == 1 and fp == 3:
                p = p + line[i]
            elif fl == 1 and fo == 5:
                o = o + line[i]
            elif fl == 1 and fu == 7:
                u = u + line[i]
            #print u
        o = o.rstrip()
        p = p[:-1]
        #print (o)
        #print (p)
        #print (u)
        p11 = p + "." + str(cnt-9999) + "> "
        p12 = p + "." + str(cnt-9999) + ".SID> "
        file2.write(s + " " + p11 + " " + o + " .\n")
        file2.write(s + " " + p12 + " " + u + " .\n")
        file2.write(p12  + "<http://www.w3.org/1999/02/22-rdf-syntax-ns#idPropertyOf> " + p11 +" .\n")
        file2.write(p11 + "<http://www.w3.org/1999/02/22-rdf-syntax-ns#companionPropertyOf> " + p + "> .\n")
        j = j+1
        cnt =cnt + 1
    print("Done.")

    f1.close()
    file2.close()

    print("File saved.")
        
