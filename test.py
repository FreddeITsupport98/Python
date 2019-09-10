
print("Välkommen till mitt program där du kan addera")

operator = input("Välj räknesätt (+ - * /): ")

try: # Try testar cod blocken
    tal1 = int(input("Mata in ett heltal: ")) #det testar tal1
except: # except kör coden om fel blir"
    print("Du måste skriva in en siffra") #print skriver ut resultat eller inskrivna input som använder har gjort
    tal1 = 0
try:
    tal2 = int(input("Mata in ett till heltal: "))
except:
    print("Du måste skriva in en siffra")
    tal2 = 0

if operator == "+": # if operator är lika med "+"
    
    summa = tal1 + tal2 

elif operator == "-": # elif operator är lika med "-"


    summa = (tal1 - tal2) 

elif operator == "*":
  
    summa = (tal1 * tal2) 

elif operator == "/":

    try: 
        summa = (tal1 / tal2) 
        
    except ZeroDivisionError: #Denna definarear noll divition som ett fel
        print("Division by 0 is not acceptable!")
   
else: 
    print("fel")

    summa = int(tal1) + int(tal2)

    print("Summan är:", summa)