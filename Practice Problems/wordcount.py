d = dict()
print("AS")
fname = input("Enter file name(without extenstion:)")
fh = open(fname + ".txt")
for line in fh:
    line = line.rstrip()
    if len(line) == 0:
        continue
    words = line.split()
    if words[0] == "From":
        time = words[5].split(":")
        d[time[0]] = d.get(time[0], 0) + 1
l = list()
for k, v in d.items():
    l.append((k, v))

l.sort()

for (k, v) in l:
    print(k, v)

# another way to print the keys and values in a dictionary
#l = list()
# for k, v in d.items():
#    l.append((v,k))

# l.sort(reverse=True)
#print("%s %d" % (l[0][1], l[0][0]))
