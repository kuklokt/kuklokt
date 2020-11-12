import matplotlib.pyplot as plt 
import numpy as np







def bytte_navn():
    valg = input("Hva vil du endre navn på? (x-akse, y-akse, graf, alt, angre) ")
    while(valg != "angre"):
        if(valg == "x-akse"):
            print("x")    
        elif(valg == "y-akse"):
            print("y")        
        elif(valg == "graf"):
            print("g")        
        elif(valg == "alt"):
            print("alt")
        valg = input("Hva vil du endre navn på? (x-akse, y-akse, graf, alt, angre) ")
    print("kan dette funke for faen")

bytte_navn()
