import random
import string

#Créer une nouvelle fenêtre sur linux ou window/mac
#Variable pour stocker ma chaines de charactères
#Variable pour stocker la taille de ma chaines de charactères
#J'ai définies la valeur de ma taille à 8 par défaut


#Fonction permettant de générer un mot de passe
def generation():
    #Variable qui stock les charactères
    #Et la Variable qui sera le résultat
    #Avec la boucle pour la longeur dans ma chaines de charactères
    equation = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
        #L'addiction de ma variable résultat avec la librarie random afin de choisir au hasard des charactères
        #et changer une variable en string, grâce à la variable déclaré en dehors de ma fonction qui était déja une string, pour définir le type de variable de mon résultat
    mot_de_passe = "".join(random.choice(equation) for i in range(8))
    return(mot_de_passe)


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


mdp = generation()

while True:
    user = input("Rentrer un MDP: ")
    if Manuellement(mot_de_passe=user):
        print("Mot de passe valide")
        break
    else:
        print("Mot de passe incorrect")
        mdp = generation()
        print(f"Mot de passe suggérer: {mdp}")
        
