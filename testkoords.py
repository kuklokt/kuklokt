import matplotlib.pyplot as plt 
import numpy as np
x_listen = []
y_listen = []
def set_punkt():
    global x_listen
    global y_listen
    grunn_liste = input("legg inn x og y separert med komma, gå videre med q \n")
    while (grunn_liste != "q"):
        grunn_liste = grunn_liste.split(",")
        x_listen.append(float(grunn_liste[0]))
        y_listen.append(float(grunn_liste[1]))
        print(x_listen[-1:] + y_listen[-1:])
        grunn_liste = input("legg inn x og y separert med komma, gå videre med q \n")
    print("Dine punkter er opprettet ")
    

set_punkt()




#x = list(map(itemgetter(0), grunn_liste)) 
 #           y = list(map(itemgetter(1), grunn_liste))