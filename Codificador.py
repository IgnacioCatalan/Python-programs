#Hecho por Ignacio Catalán

clave=['AaÁáBbCcDdEeÉéFfGgHhIiÍíJjKkLlMmNnÑñOoÓóPpQqRrSsTtUuÚúVvWwXxYyZz0123456789 .,¿?¡!:/"()-+*','fúZ4kPÍHKN!5eÉ8¿FñEógÓCcáÑ0-Do2n *qÁXjUY/)abRA1uiz:y(IV"S3s,OhvJdTWtLmMxr+.7wlBp9G?Ú¡6íQé',
       'ev-yÍ)I/Ó7ÚHGDÑapJAs,.z80¿¡QiúUfMén!(oBVE6w*L kuímqN53W4ÉYSOglÁóP1?rh2x"jTX+FcZ9KtbRád:ñC','AJ*-0RdDrtPú8?)éuóq1KzaM,:Q"xVÑCnFjíp¿y.ÁvY2e!3kÉBÓsf+ ShÍUWTiwg¡cE(bL5mGZoH9ON46I/XÚ7álñ',
       'knRY!XBwWEcúbM¿TLvmSeiI"+ñ¡5Á?uÉtJ4UQ0F8fGo,)líKó:rÓ9Ns7H.á6DéÚ*jAZqdÑ3pPÍO (aVzx-C1g/h2y','6É87ohó94Pm!Fw0:1YélrMUzcnd¡Ó¿(QZ3 WkJvCA+y5/TpÑ2iO.RbS,te?-ÁXBá)DÍaú*íHNVñg"qLÚjsIGfuExK',
       'bUlÁCgú-¿áS4?EQzÍnj DíP¡Óy/GLZpFÉ.rkhH!)8dvñ,(JmuoeXsMté1NWIRcÑ3Oi9q6VKY+*x2TfÚB0:"w57Aóa','0Ifc:HEúldON7ñMqá/6RíA8k9ÑÓ+vÁCw*YXm¡5pÚ.!,eÍ31oLBUSby"ZV¿G4ahKuÉJ-sxTFó 2zg?iérn(jP)tQDW',
       '"ápyxKÑBJúdV8isX7 ra2ñ/v?FbMz!eóf¡5Éh16A,G:0.4u¿9+QwUTOÚS*)CIPgt3RÍÓ(éDLjHíWkqmEoN-YlnÁZc','0AVNÍEyxpá7Q9zéZl,Ir:(2sMnGH¿Ú8e5"SXvq6/fÁoDubtBiC*.c+TmÓ)KhLJÉgW!¡U4R1íjwÑOdú3 kñ-Y?óFaP']
while True:
    accion=input('Para encriptar un mensaje, escribe \'e\', para desencriptar escribe \'d\': ')
    print()
    
    #codificador:
    while accion=='e':
        cod=input('Mensaje a encriptar: ')
        verif=False
        while verif==False:
            key=(input('Clave de cifrado(00-99): '))
            try:
                test=int(key)
            except:
                print('Clave de cifrado debe ser un valor entre 00 y 99, manteniendo dos dígitos')
                print()
            else:
                if len(key)!=2:
                    print('Clave de cifrado debe ser un valor entre 00 y 99, manteniendo dos dígitos')
                    print()
                else:
                    verif=True
        cont=0
        output=('')
        while cont<len(cod):
            letra=cod[cont]
            if letra in clave[0]:
                pos=clave[int(key[0])].find(letra)
                pos=pos+int(key[1])+1
                if pos>88:
                    pos=pos-89
                output=output+((clave[int(key[0])])[pos])
            else:
                output=output+letra
            cont+=1
        print('Mensaje encriptado: ',output)
        print()
        accion=''
        
    #decodificador:
    while accion=='d':
        cod=input('Mensaje a desencriptar: ')
        verif=False
        while verif==False:
            key=(input('Clave de cifrado(00-99): '))
            try:
                test=int(key)
            except:
                print('Clave de cifrado debe ser un valor entre 00 y 99, manteniendo dos dígitos')
                print()
            else:
                if len(key)!=2:
                    print('Clave de cifrado debe ser un valor entre 00 y 99, manteniendo dos dígitos')
                    print()
                else:
                    verif=True
        cont=0
        output=('')
        while cont<len(cod):
            letra=cod[cont]
            if letra in clave[0]:
                pos=clave[int(key[0])].find(letra)
                pos=pos-int(key[1])-1
                if pos<0:
                    pos=pos+89
                output=output+((clave[int(key[0])])[pos])
            else:
                output=output+letra
            cont+=1
        print('Mensaje desencriptado: ',output)
        print()
        accion=''
