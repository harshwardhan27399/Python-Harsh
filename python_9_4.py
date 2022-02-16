name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
mailers = dict()
count = 0
for line in handle:
    if line.startswith("From "):
        mailer = line.split()[1]
        mailers[mailer] = mailers.get(mailer,0)+1

max_count = None
max_word = None

for key,value in mailers.items():
    if max_count is None or max_count < value:
        max_count = value
        max_word = key

print(max_word, max_count)
