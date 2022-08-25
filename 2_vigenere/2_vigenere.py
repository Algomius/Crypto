def vigenere(c, cle):
    """
        La fonction d'encodage se base sur :
        c : le message à chiffrer sous forme de chaine de caractères
        cle : la clé à utiliser sous forme de chaine de caractères
        Elle retourne le message chiffré sous forme de chaine de caractères
    """
    indice_cle = 0
    msg_code = ""

    for i in range(0, len(c)):
        if 'A' <= c[i] <= 'Z':
            msg_code +=  chr((((ord(c[i]) - ord('A')) + (ord(cle[indice_cle]) - ord('A'))) % 26) + ord('A')) 
            indice_cle =  (indice_cle + 1) % len(cle)
        else:
            msg_code +=  c[i]
    return msg_code
    
def decode_vigenere(c, cle):
    """
        La fonction de décodage se base sur :
        c : le message chiffré sous forme de chaine de caractères
        cle : la clé à utiliser sous forme de chaine de caractères
        Elle retourne le message en clair sous forme de chaine de caractères
    """
    indice_cle = 0
    msg_code = ""

    for i in range(0, len(c)):
        if 'A' <= c[i] <= 'Z':
            msg_code +=  chr((((ord(c[i]) - ord('A')) - (ord(cle[indice_cle]) - ord('A'))) % 26) + ord('A')) 
            indice_cle =  (indice_cle + 1) % len(cle)
        else:
            msg_code +=  c[i]
    return msg_code

print(vigenere('BONJOUR A TOUS', 'PYTHON'))
print(decode_vigenere('QMGQCHG Y MVIF', 'PYTHON'))