from tkinter import *
import tkinter as tk
import random
import pyperclip
from tkinter import ttk

#Créer une nouvelle fenêtre sur linux ou window/mac
interface = tk.Tk()
#Variable pour stocker ma chaines de charactères
mdp = StringVar()
#Variable pour stocker la taille de ma chaines de charactères
longueur = IntVar()
var1 = IntVar()
var = StringVar()
#J'ai définies la valeur de ma taille à 8 par défaut
longueur.set(8)
interface.configure (background="dark blue")
interface.title("Password")
interface.geometry("600x400")


#Fonction permettant de générer un mot de passe
def generation(maj = True, min = True, penctuation = True):
    #Variable qui stock les charactères
    #Et la Variable qui sera le résultat
    #Avec la boucle pour la longeur dans ma chaines de charactères
    number = "1234567890"
    lower_case = "abcdefghijklmopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    symbol = "?#é~&!"
    equation = lower_case + upper_case + number + symbol
    mot_de_passe = ""
    for x in range(longueur.get()):
        #L'addiction de ma variable résultat avec la librarie random afin de choisir au hasard des charactères
        #et changer une variable en string, grâce à la variable déclaré en dehors de ma fonction qui était déja une string, pour définir le type de variable de mon résultat
            mot_de_passe = mot_de_passe + random.choice(equation)
    mdp.set(mot_de_passe)

#Fonction pour copier le résultat dans le presse-papier, et pouvoir le re-utilisez
def copie():
    #Je créer une variable pour récupérer mon résultat dedans
    #J'utilise la librarie pyperclip pour copier ma variable créer et l'associer à mon résultat
    random_mdp = mdp.get()
    pyperclip.copy(random_mdp)

def Manuellement():
    Taille.delete(0,END)
    length = var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
    if( var.get == 1):
        for i in range(0,length):
            password = password + random.choice(lower)
            return(password)
    elif(var.get == 0):
        for x in range(0,length):
            password = password + random.choice(upper)
            return(password)
    elif(var.get == 3):
        for o in range(0,length):
            password = password + random.choice(digits)
        return(password)
    else:
        print("choissisez un autres mot de passe")

def generate():
    password1 = Taille.get()
    Taille.insert(10,password1)






Titre = LabelFrame(interface, text="Mot de passe Automatique",borderwidth=80, relief=SUNKEN, width=60, height=200)
Titre.pack( fill=X, side=TOP, expand=True)
Taille = Entry(interface, textvariable=longueur,width=60)
Taille.place(x=50, y=100) 
Contenue = Label(interface, textvariable=mdp,borderwidth=80, relief=SUNKEN, width=70, height=70)
Contenue.pack(fill=X, side=BOTTOM, expand=True)
résultat = Label(interface,text="Résultat")
résultat.pack(fill=Y,side=RIGHT,expand=False)
résultat.place(x= 50,y=250)
Button(interface, text="Générer", command=generation,width=20).place(x=80, y=122)
Button(interface, text="Copier dans le presse-papier", command=copie, width=20).place(x=300, y=122)
interface.mainloop()



