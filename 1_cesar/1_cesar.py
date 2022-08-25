def encode_cesar(s, decalage):
    """
        La fonction d'encodage se base sur :
        s : le message à chiffrer sous forme de chaine de caractères
        decalage : valeur numérique représentant le decalage dnas l'alphabet
        Elle retourne le message chiffré sous forme de chaine de caractères
    """
    chaine_codee = ""
    for element in s:
        if 'A' <= element <= 'Z':
            indice = ord(element) - ord('A')
            indice = (indice + decalage) % 26
            chaine_codee = chaine_codee + chr(indice + ord('A'))
        elif 'a' <= element <= 'z':
            indice = ord(element) - ord('a')
            indice = (indice + decalage) % 26
            chaine_codee = chaine_codee + chr(indice + ord('a'))
        else:
            chaine_codee = chaine_codee + element

    return chaine_codee

c_code = encode_cesar('Les ennemis de l empereur meurent lentement', 3)
print(c_code)
c_clair = encode_cesar(c_code, -3)
print(c_clair)

for i in range(0,26):
    print ("décalage", i)
    print(encode_cesar(c_code, i))
    print("-------------------------------------------")

