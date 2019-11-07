print('Este programa le ayudará a determinar los divisores del número natural que elija')
while True:
    print( )
    N=int(input('Ingrese un número natural: '))
    D=1
    C=1
    print( )
    print('Divisores de ',N,': ')
    while N//2>=D:
        R=N%D
        if R==0:
            C+=1
            print (D)
        D+=1
    print(N)
    if C==2:
        print(N,'es un número primo')
    print( )
    print('Finalizado')
