name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
mailers = dict()
count = 0
for line in handle:
    if line.startswith("From "):
        mailer = line.split()[5].split(":")[0]
        mailers[mailer] = mailers.get(mailer,0)+1

lst = list()
for k,v in mailers.items():
    lst.append((k,v))

lst.sort()

for (k,v) in lst:
    print(k,v)
