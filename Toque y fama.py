import random
print('Toque y fama')
while True:
    print()
    adivinado=False
    set_n=['0','1','2','3','4','5','6','7','8','9']
    numero=[]
    random.shuffle(set_n)
    cont=0
    while cont<4:
        numero.append(set_n[0])
        set_n.remove(set_n[0])
        cont=cont+1
    numero=numero[0]+numero[1]+numero[2]+numero[3]
    numero=str(numero)
    while adivinado==False:
        sug=input('Adivina mi número: ')
        if sug==numero:
            adivinado=True
            break
        pos=0
        toque=0
        fama=0
        while pos<=3:
            if sug[pos]==numero[pos]:
                fama=fama+1
            pos=pos+1
        valor=0
        while valor<=9:
            valor=str(valor)
            if valor in (sug) and valor in (numero):
                toque=toque+1
            valor=int(valor)
            valor=valor+1
        toque=toque-fama
        if toque<=0 and fama<=0:
            print('Nada')
        elif toque==1 and fama<=0:
            print('Toque')
        elif toque<=0 and fama==1:
            print('Fama')
        elif toque>1 and fama<=0:
            print(toque,'Toques')
        elif toque<=0 and fama>1:
            print(fama,'Famas')
        elif toque==1 and fama==1:
            print('1 Toque y 1 Fama')
        elif toque>1 and fama==1:
            print(toque,'Toques y',fama,'Fama')
        elif toque==1 and fama>1:
            print(toque,'Toque y',fama,'Famas')
        else:
            print(toque,'Toques y',fama,'Famas')
    print()
    print('Has ganado!')
    print('Mi número era',numero)
    print()
    cont=input('Presiona enter para volver a jugar...')
