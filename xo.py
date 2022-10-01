grille=[['.','.','.'],['.','.','.'],['.','.','.']]
players=['X','O']
diagA=[]
diagB=[]
ok=True
indice=0
indicePlayer=[1,2]
while ok and indice<=9:
    print("\nplayer : "+str(indicePlayer[indice%2]))
    while True:
        ligne=int(input("entree la ligne de la case"))
        colonne=int(input("entree la colonne de la case"))
        if ligne==colonne:
            diagA.append(indice%2)
        if colonne+ligne==2:
            diagB.append(indice%2)
            
        if 0<=ligne<=2 and 0<=colonne<=2:
            if grille[ligne][colonne]=='.':
                grille[ligne][colonne]=players[indice%2]
                break
        print("ERROR 404")
    
        

    
    for i in range(3):
        if grille[i]==['X','X','X'] or diagA==['X','X','X'] :
            print("\nplayer 1 a gagné !!!!")
            ok=False
            break
        if grille[i]==['O','O','O'] or diagB==['O','O','O']:
            print("\nplayer 2 gagné!!!")
            ok=False
            break
    
        
    for j in range(3):
        print("|".join("".join("".join((str(grille[j]).split(",")))[1:-1].split("'")).split(" ")))
        if j!=2:
            print("------")
    indice+=1
