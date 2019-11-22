import random # importerar random module föra att generara slumpmässigt tal.

yourName = input("Hej vad heter du?: ") #namn

print("Hej" + " '" + yourName + "' " + "Du ska få spela gissa leken med  datorn. Du ska gissa mellan 1-20 och dator kommer ge dig letrådar") #introduktion


yourName = int(input("Skriv ner ett ental! för att gissa datorns nummer 1-20: ")) #användare kommer välja tal mellan 1-20

dator = random.randint(1,20) #1-20 kommer random generara vara slumpmässigt vilket är datorn

while dator != yourName: #While loop som sätter igång när användaren har valt fel nummer
    if yourName < dator: 
        print("Du har gissat för lite") #definerad ifsats om användare har gissat för lite
        yourName = int(input("Skriv ner ett ental! För att gissa datorns nummer 1-20: "))
    elif yourName > dator:
        print("Du har gissat för högt")  # definerar itsats  om användaren har gissat för högt
        yourName = int(input("Skriv ner ett ental! För att gissa datorns nummer 1-20: "))
    else: 
        break
    print("nice! du har gissat rätt") # det ska printa ut och breaka loopen.