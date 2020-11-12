import matplotlib.pyplot as plt 
import numpy as np
x_listen = []
y_listen = []

def x_navn():
    global xakse
    xakse = input("Navn på x-akse: ")
    plt.xlabel(xakse)

def y_navn():
    global yakse
    yakse = input("Navn på y-akse: ")
    plt.ylabel(yakse)

def graf_navn():
    global gnavn
    gnavn = input("Navn på graf: ")
    plt.title(gnavn)

#husk at jeg nuller ut x og y listen på starten av denne funksjonen! revurderes om jeg skal legge til flere punkter seinere
def set_punkt():
    global x_listen
    global y_listen
    grunn_liste = input("legg inn x og y separert med komma, gå videre med q ")
    while (grunn_liste != "q"):
        grunn_liste = grunn_liste.split(",")
        x_listen.append(float(grunn_liste[0]))
        y_listen.append(float(grunn_liste[1]))
        print(x_listen[-1:] + y_listen[-1:])        
        grunn_liste = input("legg inn x og y separert med komma, gå videre med q ")
    plt.plot(x_listen,y_listen)


def bytte_navn():
    valg = input("Hva vil du endre navn på? (x-akse, y-akse, graf, alt, angre) ")
    while (valg != "angre"):
        if(valg== "x-akse"):
           x_navn()
        elif(valg== "y-akse"):
         y_navn()
        elif(valg== "graf"):
            graf_navn()
        elif(valg == "alt"):
            x_navn()
            y_navn()
            graf_navn()
        elif(valg == "angre"):
            break
        valg = input("Hva vil du endre navn på? (x-akse, y-akse, graf, alt, angre) ")

def hoved_meny():
    valg = input("Velkommen til supergrafoteket! Hva vil du gjøre? Tast inn tallet på det du ønsker å gjøre. 1.Lage ny graf -  2.Hente lagret graf - 3.Endre instillinger - 4.Avslutte: ")
    while (valg != "4"):
        if(valg == "1"):
            x_navn()
            y_navn()
            graf_navn()
            set_punkt()
        elif(valg == "2"):
            break
        elif(valg == "3"):
            bytte_navn()
        valg = input("Velkommen til supergrafoteket! Hva vil du gjøre? Tast inn tallet på det du ønsker å gjøre. 1.Lage ny graf -  2.Hente lagret graf - 3.Endre instillinger - 4.Avslutte: ")
    print("snakkes")
    plt.show()

hoved_meny()









