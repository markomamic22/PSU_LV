ocjena = -1.0
while ((ocjena < 0.0) or (ocjena > 1.0)):
    ocjena = float(input("Unesite broj između 0 i 1: "))

def cases(ocjena):
    if(ocjena>=0.9): print('A')
    elif(ocjena>=0.8): print('B')
    elif(ocjena>=0.7): print('C')
    elif(ocjena>=0.6): print('D')
    elif(ocjena<0.5): print('F')

cases(ocjena)