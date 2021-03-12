import sys

string = "False"
sum = 0
min_num = sys.maxsize
max_num = 0
count=0
while (string != "Done"):
    try:
        string = input()
        number = int(string)
        sum += number
        if(min_num > number):
            min_num = number
        if(max_num < number):
            max_num = number
        count += 1
    except ValueError:
        
        print("Unesite ili broj ili \"Done\"")    

print("Unijeli ste",count,"brojeva")
print("Srednja vrijednost je:",(sum/count))
print("Minimalna vrijednost je:",min_num)
print("Maksimalna vrijednost je:",max_num)

                

