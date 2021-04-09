for angka in range(10,25):
    for n in range(2,angka):
        if angka % 2 == 0 or angka % 3 == 0 or angka % 5 == 0 or angka % 7 == 0:
            print(angka,"bukan prima.")
            break
        else:
            print(angka,"adalah bilangan prima.")
            break

