print('Este programa determinará los primeros N números de la secuencia de Fibonacci,')
print('siendo N la cantidad que usted elija.')
while True:
    N=int(input('Cuántos números de Fibonacci quiere imprimir?: '))
    a=1
    b=1
    print(a)
    print(b)
    cont=2
    while N>cont:
        a=a+b
        print(a)
        cont=cont+1
        if cont>=N:
            break
        b=a+b
        print(b)
        cont=cont+1
    print( )
    razon=a/b
    if razon>1:
        print('con los dos últmos valores, la razón de Fibonacchi es: ',1/razon)
    else:
        print('Con los dos últmos valores, la razón de Fibonacchi es: ',razon)
    print( )
    print('Mientras más grandes son los números de Fibonacci usados, más se acerca esta')
    print('razón a la proporción aúrea.')
    print( )
