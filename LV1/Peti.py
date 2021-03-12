import os
import pathlib


name = input("Unesite ime datoteke:")
name = os.path.abspath(name)
fhand = open(name)
sum = 0.0
counter = 0

for line in fhand:
    line =  line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        number = float(line.find(": "))
        sum += number
        counter +=1
print("Srednja vrijednost je:",float(sum/counter))        
