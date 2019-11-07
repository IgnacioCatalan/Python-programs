import random
import time
arma=['una espada','una pistola NERF','unos nunchaku','el poder de la amistad','una ametralladora','unas dagas','un UWU','un arco',
      'la deprimente realidad de nuestra existencia','una lanza','una cachetada','un sable láser','una piedra que encontró por ahí',
      'un martillo de guerra','una porotera','una bebida Tula','un plátano','un caparazón azul','una bola de fuego mágica',
      'un machete','un Rasengan','una motosierra','sus puños']
dano=[30,20,15,35,40,15,30,20,50,25,10,35,9,40,10,15,10,50,70,35,40,45,10]
print('Duelo de Titanes')
while True:
    starter=random.randint(1,2)
    HP1=100
    HP2=100
    print()
    P1=input('Nombre del primer luchador: ')
    P2=input('Nombre del segundo luchador: ')
    print()
    print('En esta batalla:',P1,'VS',P2,'!!!')
    print()
    print(P1,':',HP1,'HP')
    print(P2,':',HP2,'HP')
    time.sleep(3)
    print()
    if starter==2:
        pick=random.randint(0,len(arma)-1)
        atk=arma[pick]
        hit=random.randint(dano[pick]-8,dano[pick]+8)
        print(P2,'ataca con',atk,'e inflinge',hit,'puntos de daño a',P1)
        HP1=HP1-hit
        if HP1>0:
            print(P1,':',HP1,'HP')
            print(P2,':',HP2,'HP')
            print()
            time.sleep(5)
    while HP1>0 and HP2>0:
        pick=random.randint(0,len(arma)-1)
        atk=arma[pick]
        hit=random.randint(dano[pick]-8,dano[pick]+8)
        print(P1,'ataca con',atk,'e inflinge',hit,'puntos de daño a',P2)
        HP2=HP2-hit
        if HP2<=0:
            break
        print(P1,':',HP1,'HP')
        print(P2,':',HP2,'HP')
        print()
        time.sleep(5)
        pick=random.randint(0,len(arma)-1)
        atk=arma[pick]
        hit=random.randint(dano[pick]-8,dano[pick]+8)
        print(P2,'ataca con',atk,'e inflinge',hit,'puntos de daño a',P1)
        HP1=HP1-hit
        if HP1<=0:
            break
        print(P1,':',HP1,'HP')
        print(P2,':',HP2,'HP')
        print()
        time.sleep(5)
    if HP2<=0:
        print(P1,':',HP1,'HP')
        print(P2,': 0 HP')
        time.slee(2)
        print()
        print(P1,'ha ganado!')
    if HP1<=0:
        print(P1,': 0 HP')
        print(P2,':',HP2,'HP')
        time.sleep(2)
        print()
        print(P2,'ha ganado!')
    print()
    restart=input('Presiona Enter para iniciar otra batalla')
