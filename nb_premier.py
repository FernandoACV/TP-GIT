# Liste des nombres premier de 1 à 100000
 
def nb_premier(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
 
# main
bx=False
by=False
while(bx==False):
    x = int (input("entrez un nombre entier positif supérieur à 0 : "))
    if (x>0):
        bx=True 
    else:
        print("veuillez entrer un nombre valide")
while(by==False):
    y = int (input ("entrez un nombre entier positif supérieur au précédent : "))
    if (y>x):
         by=True
    else:
        print("veuillez entrer un nombre valide")

lst = nb_premier(x, y)
if len(lst) == 0:
    print("Il n'y a pas de nombres premier dans cet intervalle")
else:
    print("Les nombres premier sont: ", lst)