
with open("map.vmf", "rt") as fin:
    data = fin.read()

    datalist = data.split('\n')
for i in range (0,len(datalist)):
    newposition = 0
    position = 0
    data2 = ""
    if '"lightmapscale"' in datalist[i]:
        temp = datalist[i]
        datalist[i] = (temp+'\n            "rotation" "0"\n')
with open("map.vmf",'w') as fout:
    for i in range (0,len(datalist)):
        fout.write(datalist[i]+"\n")
print("Done!")
