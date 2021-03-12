
mailing_list = []
hostname_dictionary = {}
try:
    fhand = open("LV1\mbox-short.txt")
except:
    exit()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From"):

        if(line[4] == ':'):
            start = line.find(":")
            mail = line[(start+2):]
            if(mail not in mailing_list):
                mailing_list.append(mail)
        elif(line[4] == ' '):
            start = line.find(" ")
            mail = line[(start)+1:]
            start_space = mail.find(" ")
            mail = mail[:start_space]
            if(mail not in mailing_list):
                mailing_list.append(mail)



for i in range(len(mailing_list)):
    line = mailing_list[i]
    start_at = line.find("@")
    line = line[(start_at+1):]
    if(line not in hostname_dictionary):
        hostname_dictionary[line] = 1
    elif(line in hostname_dictionary):
        hostname_dictionary[line] += 1

print("Nekoliko spremljenih mailova:\n")
i = 0
for i in range(3):
    print(mailing_list[i])
print("\nBroj ponavljanja hostnamea:")
for x,y in hostname_dictionary.items():
    print (x,":",y)