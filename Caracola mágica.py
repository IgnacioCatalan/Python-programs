import random
continuar=True
print('La caracola mágica')
while continuar==True:
    print()
    question=input('Pregúntale algo a la Caracola Mágica: ')
    print()
    print('La Caracola dice:')
    answer=random.randint(1, 20)
    if answer==1:
        print('Si')
    elif answer==2:
        print('No')
    elif answer==3:
        print('Totalmente')
    elif answer==4:
        print('Voh dale')
    elif answer==5:
        print('Claro por qué no')
    elif answer==6:
        print('Imposible')
    elif answer==7:
        print('Tai webiando cierto...?')
    elif answer==8:
        print('Eh... si?')
    elif answer==9:
        print('Puede ser')
    elif answer==10:
        print('No lo sé')
    elif answer==11:
        print('Solamente depende de tí, eres el único capaz de forjar tu propio futuro,')
        print('PUEDES HACERLO! NUNCA TE RINDAS, TIENES EL MUNDO EN TUS MANOS!!')
    elif answer==12:
        print('No lo creo')
    elif answer==13:
        print('Probablemente')
    elif answer==14:
        print('Probablemente no')
    elif answer==15:
        print('No me interesa, pregúntale a alguien más')
    elif answer==16:
        print('Créeme, no quieres saber la respuesta')
    elif answer==17:
        print('Uff ni te imaginas')
    elif answer==18:
        print('Ciertamente')
    elif answer==19:
        print('Ni cagando')
    else:
        print('Completamente, es que no necesitas ni preguntarme')
    print()
    print('Ha hablado la Caracola Mágica')
    print()
    verif=input('Quieres hacer otra pregunta?(si/no): ')
    if verif=='no':
        continuar=False
              
