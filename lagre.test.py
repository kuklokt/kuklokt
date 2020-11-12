import os
import time
#!!!!!!!!!HUSK HVOR VI MÅ LUKKE FILEN ETTER BRUK og sette hva som skal skje etter prosess er avsluttet
#oppretter filnavn
def lagre_fil():
    open_navn = input("Skriv inn ønsket filnavn: ")
    while (open_navn != ""):
        skrive.fil = open(open_navn + ".txt", "w")
    print("Ugyldig... Prøv igjen ")
    lagre_fil()
    




#slette funksjon
def slette_fil():
    vismeg()
    slette_navn = input("Skriv kun filnavn, uten .txt på den du ønsker å slette, blankt for å gå tilbake: ")
    while(slette_navn != ""):
        if os.path.exists(slette_navn + ".txt"):
            os.remove(slette_navn + ".txt")
        elif(slette_navn == ""):
            slette_fil()
        #hva som skal skje når brukeren angrer
    print("Finner ikke filen, prøv igjen...")
    time.sleep(1)
    slette_fil() 


#vise alle filene i root
def vismeg():
    print("Lagrede filer: ")
    arr_txt = [x for x in os.listdir() if x.endswith(".txt")]
    print(arr_txt)


