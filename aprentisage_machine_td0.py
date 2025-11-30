def pascal_somme(n):
    somme_diag = [1]
    # Pascal sera une liste de lignes, chaque ligne est une liste d'entiers
    Pascal = [[1]]
    # Construire les lignes 1 par 1 en s'appuyant sur la ligne précédente
    for i in range(1, n):
        prev = Pascal[-1]
        # commencer la nouvelle ligne par 1
        row = [1]
        # calculer les éléments intérieurs comme somme des deux éléments au-dessus
        for j in range(1, len(prev)):
            row.append(prev[j - 1] + prev[j])
        # terminer la ligne par 1
        row.append(1)
        Pascal.append(row)

    for row in Pascal:
        for number in row:
            print(number, end = " ")  
        print()
    
    for k in range(1,n):
        s=0
        j=0
        while j < len(Pascal[k-j]) and k-j >=0:
            s += Pascal[k-j][j]
            j += 1
        somme_diag.append(s)
    print(somme_diag)


def matrice_spirale(n, m):
    M= np.zeros((n,m))
    h = 0
    d = m-1
    b = n-1
    g = 0
    num = 1

    while h<=b and g<=d:
        for col in range(g,d+1):
            M[h][col]=num
            num += 1
        h += 1

        for lig in range(h, b+1):
            M[lig][d]= num
            num += 1
        d -= 1

        for col in range(d, g-1, -1):
            M[b][col] = num
            num +=1
        b -=1

        for lig in range ( b, h-1, -1):
            M[lig][g] = num
            num += 1
        g += 1

    print(np.array(M))

# déclaration de fonction:
pascal_somme(10)
matrice_spirale(8,9)