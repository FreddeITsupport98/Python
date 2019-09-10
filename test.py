
print("Välkommen till mitt program där du kan addera")
try:
    tal1 = int(input("Mata in ett heltal: "))
except:
    print("Du måste skriva in en siffra")
    tal1 = 0
try:
    tal2 = int(input("Mata in ett till heltal: "))
except:
    print("Du måste skriva in en siffra")
    tal2 = 0

summa = tal1 + tal2
print("Summan är:", summa)