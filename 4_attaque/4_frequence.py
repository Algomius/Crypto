def donne_frequence(s):
    """
    La fonction donne_frequence prend une chaine de caractères en paramètre et affiche
    la répartition des lettres dans la chaine.
    """
    freq = {}
    for element in s:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1

    for k, v in freq.items():
        print(k, v /len(s))

donne_frequence('Ohv hqqhplv gh o hpshuhxu phxuhqw ohqwhphqw')