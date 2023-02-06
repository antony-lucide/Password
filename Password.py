import random
import string
import adafruit_hashlib as hashlib


def generation():
    #Variable qui stock les charactères
    #Et la Variable qui sera le résultat
    #Avec la boucle pour la longeur dans ma chaines de charactères
    #L'addiction de ma variable résultat avec la librarie random afin de choisir au hasard des charactères
    #L'import du string permet de raccourcir les chaines de charactère qui sont deja prédefinis grâce à cette librairie
    equation = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
    mot_de_passe = "".join(random.choice(equation) for i in range(8))
    return(mot_de_passe)

#Condition permettant de vérifier si l'input donner par l'utiliseur est valide, en vérifiant la majuscule,la minuscule, et le chiffre
def Manuellement(mot_de_passe):
    if len(mot_de_passe) != 8:
            return False
    if not any(char.isdigit() for char in mot_de_passe):
        return False
    if not any(char.isupper() for char in mot_de_passe):
        return False
    if not any(char.islower() for char in mot_de_passe):
        return False
    else:
        return True

#Je déclare d'abord que la variable "mdp", est l'instance de ma fonction generation
#Ensuite j'encode une variable qui me permettra  d'encoder mon mot de passe crypté entré par l'user et un mot de passe suggérer
#Ensuite je définies une condition pour vérifier si l'user respecte les Majuscules, Minuscules, et chiffres,penctuations
#Si les conditions sont réspecter alors je print le mot de passe génerer cripter
#Si les conditions sont pas réspecter alors je lui suggère un mot de passe valide
mdp = generation()
Password = hashlib.sha256(mdp.encode('utf-8')).hexdigest()
while True:
    user = input("Rentrer un MDP: ")
    user = hashlib.sha256(mdp.encode('utf-8')).hexdigest()
    if Manuellement(user):
        print("Mot de passe valide")
        print("Mot de passe cripté: ", user)
        break
    else:
        print("Mot de passe incorrect")
        mdp = generation()
        print(f"Mot de passe suggérer: {Password}")
        
