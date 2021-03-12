
mailing_list = []

try:
    fhand = open("LV1\mbox-short.txt")
except:
    exit()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        start = line.find(":")
        mail = line[(start+2):]
        atstart = mail.find("@")
        hostname = mail[(atstart+1):]
        mailing_list.append(mail)
        
        
         
       

i = 0        
for i in range(len(mailing_list)):
    print(mailing_list[i])



