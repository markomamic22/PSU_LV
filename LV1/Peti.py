import os
import pathlib


# D:\GitHub Repos\PSU_LV\LV1\mbox.txt - prava putanja
# 'D:\\GitHub Repos\\PSU_LV\\mbox.txt' - putanja dobivena kroz program

# iz nekog razloga mi ne radi dobivanje patha kroz program - radi ako predam umjesto imena datoteke putanju
name = input("Unesite ime datoteke:")
name = os.path.abspath(name)
try:
    fhand = open(name)
except:
    exit()
sum = 0.0
counter = 0

for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        start = line.find(":")
        number = float(line[(start+2):])
        sum += number
        counter += 1
print("Srednja vrijednost je:", float(sum/counter))
