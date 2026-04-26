mine = [[7,  9, 10,  7, 10,  8,  5],
        [5,  3,  1,  7,  5,  7,  1],
        [8,  9,  7,  7,  2,  3,  2],
        [7,  7,  2,  4,  6,  5,  7],
        [6,  7,  1,  6,  6,  6,  1],
        [3,  2,  5,  3,  2,  2, 10]]

memo = None

def dimensions(mine):
    """Renvoie le tuple (hauteur, largeur) de la mine"""
    return len(mine), len(mine[0])



def meilleur_richesse_cummulees(mine, etage, rang, memo):
    x_max, y_max = dimensions(mine)

    if memo is None:
        memo = {}

    if etage == x_max : #si le block est de la derniere ligne il na pas de precedent et donc 
        return mine[etage][rang] # on renvoi ca valeur pour la recurtion pas besoin de l'ajouter au memo
    
    if mine[etage][rang] in memo :
        return memo[mine[etage][rang]]
    
    if rang == 0 :
        memo[mine[etage, rang]] = max( 
        meilleur_richesse_cummulees(mine, etage+1, rang, memo), 
        meilleur_richesse_cummulees(mine, etage+1, rang + 1, memo))

    if rang == y_max :
        memo[mine[etage][rang]] = max(
        meilleur_richesse_cummulees(mine, etage+1, rang -1,memo), 
        meilleur_richesse_cummulees(mine, etage+1, rang, memo))

    memo[mine[etage][rang]] = max(
    meilleur_richesse_cummulees(mine, etage+1, rang -1,memo), 
    meilleur_richesse_cummulees(mine, etage+1, rang,memo), 
    meilleur_richesse_cummulees(mine, etage+1, rang + 1,memo))

    return max(memo.values)



print(meilleur_richesse_cummulees(mine, 0, 0, memo))



            








    
