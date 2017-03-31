f = open("jscore_final","w")

for i in range(17):
    f1 = open("ChangeLog%d"%i,"r")
    all = f1.read()
    f.write(all)
    f1.close()

f.close()
