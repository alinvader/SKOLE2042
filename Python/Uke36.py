#Steg 1: Python kan vise verdier
print("Hei")
print(5)
#--------------------------------------
#småoppgave: Begge ser like ut på skjermen, men Python behandler dem forskjellig.
"Ali"
print("5")
print(5)

#Steg 2: Variabler gir verdier navn
#ventre side navn på variabelen. På høyre side verdien som lagres
navn = "Sara"
alder = 32
print(navn)
print(alder)
#------------------------------------------------------------------

#Oppgave 1 – lag og bruk variabler:
navn = "Ali"
alder = "33"
bosted = "Oslo"
print(navn)
print(alder)
print(bosted)
#------------------------------------------------------------------

#Steg 3: Vi kan regne med variabler
pris = 30
antall = 3
total = pris * antall
print(total)
#------------------------------------------------------------------

#Oppgave 2 – fra faste verdier til beregning:
Bil = 127000
tilhenger = 10000
total = Bil + tilhenger
print(total)
#-----------------------------------------------------------------

#Steg 4: input lar brukeren skrive inn en verdi
#input() stopper programmet og venter på at brukeren skriver noe. Først bruker vi input bare som tekst.
#-----------------------------------------------------------------

#Oppgave 3: spør etter navn og bosted
print("Hva heter du?")
navn = input()

print("Hvor bor du? ")
bosted = input()

print("Hvor lenge har du vært i Norge? ")
periode = input()

print(navn, "bor i", bosted, "og har vært", periode)