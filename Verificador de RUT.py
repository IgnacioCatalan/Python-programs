while True:
    correct=False
    while correct==False:
        RUT=input('Ingrese su rut sin puntos ni guión: ')
        if (len(RUT)==8 or len(RUT)==9) and ('.' not in (RUT)) and ('-' not in (RUT)):
            print()
            correct=True
        else:
            print('Por favor ingrese un rut válido')
            print()
    i=len(RUT)-2
    mul=1
    rut=[]
    while i>=0:
        mul=mul+1
        factor=int(RUT[i])*mul
        rut.append(factor)
        i=i-1
        if mul>=7:
            mul=1
    suma=sum(rut)
    DV=str(11-suma%11)
    i=len(RUT)-1
    if DV==RUT[i]:
        print('Este rut es correcto')
    elif DV=='11' and RUT[i]=='0':
        print('Este rut es correcto')
    elif DV=='10' and RUT[i]=='k' or RUT[i]=='K':
        print('Este rut es correcto')
    else:
        print('Este rut no existe')
    print()
