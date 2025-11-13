"""Le programme à pour but principal ispalindrome() qui renvoie la valeur de la question
    La chaine passer een paramètre est elle un palindrome ?
    """
#### Fonction secondaire


def ispalindrome(p):
    """fonction : teste si la chaine passer en paramètre est un palindrome
        Paramètre : 
            p : la chaine tester
        Return : 
            true : si la chaine est un palindrome
            false : si elle ne l'est pas
        """
    table = str.maketrans({
    'à': 'a', 'â': 'a', 'ä': 'a',
    'á': 'a', 'ã': 'a', 'å': 'a',
    'ç': 'c',
    'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
    'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
    'ñ': 'n',
    'ó': 'o', 'ò': 'o', 'ô': 'o', 'ö': 'o', 'õ': 'o',
    'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
    'ý': 'y', 'ÿ': 'y', ' ' : None, ',' : None, ';' : None
    , '!' : None, '.' : None, '?' : None, '"' : None, '-' : None, '\'' : None
    , ':' : None
    })
    p = str(p).lower().translate(table)
    return p == p[::-1]

#### Fonction principale


def main():
    """main ddu programme : teste l'appel de ispalindrome()"""
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie", "é pé"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
