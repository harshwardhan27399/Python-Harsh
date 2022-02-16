# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        pos = line.find(':')
        num_value = float(line[pos+1:].strip())
        total = total + num_value
        count += 1

average_spam_c = total / count
print("Average spam confidence: ",average_spam_c)
