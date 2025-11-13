#### Fonction secondaire
 

def ispalindrome(p):
    p = p.lower
    traduction_table = str.maketrans({
    # Lettres minuscules
    'à': 'a', 'â': 'a', 'ä': 'a',
    'á': 'a', 'ã': 'a', 'å': 'a',
    'ç': 'c',
    'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
    'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
    'ñ': 'n',
    'ó': 'o', 'ò': 'o', 'ô': 'o', 'ö': 'o', 'õ': 'o',
    'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
    'ý': 'y', 'ÿ': 'y',
    })
    word = p.translate(traduction_table)
    print(word)
    return False

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie", "épée"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()