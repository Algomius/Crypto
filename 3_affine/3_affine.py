def affine(s, a, b):
    """
        La fonction d'encodage se base sur :
        s : le message à chiffrer sous forme de chaine de caractères
        a : Le coefficient directeur de la fonction y = a.x + b
        b : L'ordonnée à l'origine de la fonction y = a.x + b
        Elle retourne le message chiffré sous forme de chaine de caractères
    """
    chaine_codee = ""
    for e in s:
        indice = ord(e) - ord('A')
        indice = (indice * a + b) % 26
        chaine_codee += chr(indice + ord('A'))

    return  chaine_codee

def decode_affine(s, a, b):
    """
        La fonction de décodage se base sur :
        s : le message chiffré sous forme de chaine de caractères
        a : Le coefficient directeur de la fonction y = a.x + b
        b : L'ordonnée à l'origine de la fonction y = a.x + b
        Elle retourne le message en clair sous forme de chaine de caractères
    """
    chaine_codee = ""
    for e in s:
        indice = ord(e) - ord('A')
        indice = ((indice - b)*a) % 26
        chaine_codee += chr(indice + ord('A'))

    return  chaine_codee

print(affine('BONJOUR', 3, 9))
print(decode_affine('MZWKZRI', 9, 9 ))
