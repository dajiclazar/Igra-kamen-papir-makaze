import random

igrac = 0
cpu = 0

while True:
    igra = ["makaze", "papir", "kamen"]

    izbor2 = random.choice(igra)

    izbor = input("Upisite papir, kamen ili makaze (Upisite q za izlazak): ").lower()
    if izbor == "q":
        break
        exit()

    if izbor == "papir" and izbor2 == "papir":
        print("Racunar je izabrao papir")
        print("Nereseno")
        continue

    if izbor == "papir" and izbor2 == "kamen":
        print("Racunar je izabrao kamen")
        print("Pobedili ste")
        igrac += 1
        continue

    if izbor == "papir" and izbor2 == "makaze":
        print("Racunar je izabrao makaze")
        print("Izgubili ste")
        cpu += 1
        continue
    if izbor == "kamen" and izbor2 == "papir":
        print("Racunar je izabrao papir")
        print("Izgubili ste")
        cpu += 1
        continue
    if izbor == "kamen" and izbor2 == "kamen":
        print("Racunar je izabrao kamen")
        print("Nereseno")
        continue
    if izbor == "kamen" and izbor2 == "makaze":
        print("Racunar je izabrao makaze")
        print("Pobedili ste")
        igrac += 1
        continue
    if izbor == "makaze" and izbor2 == "papir":
        print("Racunar je izabrao papir")
        print("Pobedili ste")
        igrac += 1
        continue
    if izbor == "makaze" and izbor2 == "kamen":
        print("Racunar je izabrao kamen")
        print("Izgubili ste")
        cpu += 1
        continue
    if izbor == "makaze" and izbor2 == "makaze":
        print("Racunar je izabrao makaze")
        print("Nereseno")
        continue

print("Igrac je imao: ",  igrac  ,"poena")
print("Racunar je imao: ",  cpu ,"poena")

if igrac > cpu :
    print("Igrac je pobedio")
    print("Cestitamo")

elif cpu > igrac: print("Racunar je pobedio, vise srece sledeci put ")

else: print("Nereseno")