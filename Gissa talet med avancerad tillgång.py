import random
#detta .py filen har insperarats av https://enlight.nyc/projects/guess-number/

gissningar = 0 # definerar  med värde noll

name = input("Hej och välkommen till gissa leken 2.0, vad heter du?: /n") # namn input
print("Hej"+ " " + name + " " + ", jag tänker på en heltal. Kan du gissa det? /n") # printar ut text

svårighet = input("Hej, innan du spelan startar "+ name + ". Vilken svårighetesgrad vill du spela ? [lätt: 1-20] eller [mellan: 1-50] eller [svår: 1000]:  " # ger användaren val på svårigheten

if svårighet == lätt: # har problem vet inte varför 
    siffra = random.randint (1,20) #lätt nivå
    chans = 8 #standard antal chanser 
    print ("Okay, " + name + ". Jag tänker på en siffra mellan 1 and 20")
elif svårighet == mellan:
    siffra = random.randint (1,50)
    chans = 15 # mellan nivå med fler chanser
    print ("Okay, " + name + ". Jag tänker på en siffra mellan 1 and 50")
elif svårighet == svår:
    siffra = random.randint (1,100)
    chans = 20 # svår nivå med fler chanser att gissa
    print ("Okay, " + name + ". Jag tänker på en siffra mellan 1 and 100")    
else:
  print("välj minst av svårigheterna")

while gissningar < chans: # medans gissningar är mindre än chans sä kan spelare fortsätta
  gissar = input("Ta en gissning: ") 
  gissar = int(gissar) # # converterar till intenger för att undvika typerror

  gissningar = gissningar + 1 #varje gissningar som görs kommer det räknas som siffra 1 
  gissnarKvar = chans - gissningar # varje chans enlingt svårighetsgraden - talet 1 alltså lätt är 8 chanser - 1 gissningar = 7 chanser

  if gissar < siffra: # om datorn siffra är större än användarens gissning kommer printa ut en lettråd
    gissnarKvar = str(gissnarKvar)
    print("Din gissning är för låg! Du har " + gissnarKvar + " gissnar kvar")
    
  elif gissar < siffra: # om datorn siffra är mindre än användarens gissning kommer printa ut en lettråd
     gissnarKvar = str(gissnarKvar)
     print("Din gissning är för högt! Du har " + gissnarKvar + " gissnar kvar")

  elif gissar == siffra: # när användaren gissar rätt kommer loopen breaka
      break
if gissar == siffra: # med användarens gissning utav summan e.g: 8 är rätt tal ska printa och antal försök användaren har gjort
  gissnarKvar = str(gissnarKvar) # converterar till sträng för att undvika typerror
  print("bra jobbat du har gissat siffran " + gissnarKvar + " med antal försök") #contaterar antal försök e.g: 5 antal försök

if gissar != siffra: # Om användaren gissar för många gånger och har löpt ur antal försök kommer loopen breaka till "siffran inte lika med antal gissningar" 
  siffra = str(siffra)  # converterar till sträng för att undvika typerror
  print("ÅÅnej. Siffran jag tänkte på var " + siffra + " ;)") #svaren ska komma fram 