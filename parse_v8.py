'''
f = open("v8_ChangeLog", "r")
f1 = open("v8_log", "w")

l = f.readline()
while True:
    change = []
    while True:
        if l != "" and l != "\n" and "Performance and stability improvements" not in l:
            change.append(l.strip())
        l = f.readline()
        if l[:2] == "20":
            break
    if len(change) > 1:
        for i in range(len(change)):
            f1.write(change[i]+"\n")
        print change

f.close()
f1.close()
'''

f = open("v8_log2", "r")
f1 = open("v8_log3", "w")

l = f.readline()
prev = l.split()[2].split(".")[:2]

while True:
    f1.write("\nVERSION " + ".".join(l.split()[2].split(".")[:2]) + "\n")
    while True: 
        l = f.readline()
        if l[:2] == "20":
            curr = l.split()[2].split(".")[:2]
            if curr == prev:
                pass
            else:
                prev = curr
                break
        else:
            f1.write(l.strip() + "\n")
    #raw_input()

f.close()
f1.close()



