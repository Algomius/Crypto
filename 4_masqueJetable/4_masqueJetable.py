import random

def masque_jetable(c, cle):
    """
        La fonction d'encodage se base sur :
        c : le message à chiffrer sous forme de chaine de caractères
        cle : La clé générée aléatoirement sous forme de liste d'entiers
        Elle retourne le message chiffré sous forme de liste de caractères
    """
    msg_code = [None] * len(c)

    for i in range(0, len(c)):
        msg_code[i] = chr(ord(c[i]) ^ cle[i])
    return msg_code
    
message = 'COUCOU'

#Generation de len(message) nombres aléatoires entre 0 et 255 (8 bits)
alealist = random.sample(range(0, 256), len(message))

chiffrage = masque_jetable(message, alealist)
print(chiffrage)
decryptage = masque_jetable(chiffrage, alealist)
print(decryptage)