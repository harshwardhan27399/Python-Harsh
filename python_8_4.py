fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.strip().split()
    for content in words:
        if content not in lst:
            lst.append(content)
lst.sort()
print(lst)
