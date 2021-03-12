sati = int(input('Unesite radne sate:'))
zarada = int(input("Koliko ste plaćeni po satu:"))


def total_kn(sati, zarada):
    rez = sati * zarada
    return rez


print("Zaradili ste:\n", total_kn(sati, zarada), "kn")
