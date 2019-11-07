print('Este programa busca todos los números primos existentes por debajo del valor que elijas')
while True:
    N=int(input('Buscar números primos por debajo de: '))
    print( )
    D=2
    Cont=0
    while D<=N:
        V=2
        while V<=D:
            if V==D:
                print(D)
                Cont=Cont+1
                break
            elif D%V!=0:
                V=V+1
            else:
                break
        D=D+1
    print( )
    if Cont==1:
        print(Cont,'número primo encontrado')
    else:
        print(Cont,'números primos encontrados')
    print( )
    print('Finalizado')
    print( )
