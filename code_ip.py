"""

Exercice :

    - Ce programme permet de tester la compatibilité de deux IP dans un réseau local

Definition :

    - Si le masque sous reseau est 255.255.255.0 (ou 24) (les 3 premiers octets doivent être identiques)
    - Si compatible veut dire que les 2 IP peuvent être utiliser dans le même réseau (car je suis pas sur de repondre correctement au sujet)

Exemple d'utilisation :
        
    # Test bruteforce :

        Experience(int(input("Nombre d'essais : "))

    # Test avec deux IP données :

        nombre = None, ne sert à rien
        tuple = ([192,168,1,1], [192,168,1,2]) # IP1, IP2

        Experience(1, tuple)

"""

# Imports :

import random

# Fonctions :

def Compatibles(ip): 
    IP1 = ip[0]
    IP2 = ip[1]

    if IP1[0:3] == IP2[0:3]: # Si les trois premiers octets sont identiques (192.168 ou autre)
        return True
    else:
        return False
    
def GenererIPv4():
    IP = []
    for i in range(4): # Generation d'une IP en 4 etapes pour chaque octet
        IP.append(random.randint(0, 255))   
    return IP
 
def Experience(trys = None, ipDonné = None): # = None pour que les parametres soient optionnels 

    if ipDonné != None: # Si deux IP sont données
        if Compatibles(ipDonné):
            print("les deux IP donné sont compatibles")
        else:
            print("Les deux IP donné ne sont pas compatibles")

        return None # Fin de la fonction
    else:
        print("Test bruteforce (ne print pas les IP non compatibles)")

    for i in range(trys): # Test bruteforce
        Ips = [GenererIPv4(), GenererIPv4()]
        if Compatibles(Ips):
            print("+1 Compatibilite")
            print(Ips)
    
# Exemple d'utilisation dans le cas d'un test de compatibilité avec deux IP données :

tuple = ([192,168,1,1], [192,168,1,2]) # IP1, IP2

Experience(None, tuple)
