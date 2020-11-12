#my_file = open(filename, mode)

#bruker os for å liste alle .txt filer
import os
#funksjon for å vise alle .txt filer i root
def vismeg():
    arr_txt = [x for x in os.listdir() if x.endswith(".txt")]
    print(arr_txt)




gjeste_liste = []

gjest = input("skriv inn navn på gjest, eller exit ")
while (gjest != "exit"):
    #legg til gjesten i gjeste-listen
    gjeste_liste.append(gjest + "\n")
    gjest = input("skriv inn navn på gjest, eller exit ")

#lag fil gjester.txt og skriv til den
skrive_fil = open("gjester.txt", "w")

#skriv en etter en gjest. X tar på seg gjestenavn
for x in gjeste_liste:
    skrive_fil.write(x)

#lukk filen
skrive_fil.close()

#prøv å åpne gjester.txt, i lesemodus
lese_fil = open("gjester.txt", "r")

#les hele filen, lagre i gjester variabelen
gjester = lese_fil.read()

print(gjester)


#må sikkert gi hver info en unik plass, for så å hente