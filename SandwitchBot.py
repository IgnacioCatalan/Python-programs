import random
import time
print('SandwitchBot')
pan=1
up=0
dn=0
while True:
    print()
    x=random.randint(0,1)
    print('Cae el sandwitch número',pan)
    if x==0:
        print('Ha caído con la palta hacia arriba')
        up=up+1
    if x==1:
        print('Ha caído con la palta hacia abajo')
        dn=dn+1
    pan=pan+1
    print()
    print('Sandwitches sobrevivientes:',up)
    print('Sandwitches muertos:',dn)
    time.sleep(3)
