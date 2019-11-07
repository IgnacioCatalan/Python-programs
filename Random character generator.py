import random
cont=True

print('This program will help you create a character with random basic information, to play with in rol')
print('playing tabletop games like D&D.')
print('You can straight use the character created in your games or you can use it as inspiration to')
print('create your own.')

while cont==True:
    race=['Human', 'Elf', 'Half-elf', 'Orc', 'Half-orc', 'Halfling', 'Dwarf', 'Dragonborn', 'Gnome', 'Merfolk']
    clas=['Fighter', 'Paladin', 'Rogue', 'Ranger', 'Barbarian', 'Monk', 'Wizard', 'Sorcerer', 'Cleric', 'Warlock', 'Druid', 'Bard']
    alignment_1=['Lawful', 'Neutral', 'Chaotic']
    alignment_2=['Good', 'Neutral', 'Evil']
    
    print()
    Name=input('Choose a name for your character: ')
    
    c_race=random.choice(race)
    c_class=random.choice(clas)
    c_alignment1=random.choice(alignment_1)
    c_alignment2=random.choice(alignment_2)
    if c_alignment1=='Neutral' and c_alignment2=='Neutral':
        alignment=('True Neutral')
    else:
        alignment=(c_alignment1+' '+c_alignment2)
    
    stre=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    dex=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    con=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    inte=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    wis=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    cha=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    
    print()
    print(Name,'\'s character sheet: ')
    print()
    print('Race:',c_race)
    print('Class:',c_class)
    print('Alignment:',alignment)
    print('Abilities:')
    print('  Strength:',stre)
    print('  Dexterity:',dex)
    print('  Constitution:',con)
    print('  Inteligence:',inte)
    print('  Wisdom:',wis)
    print('  Charisma:',cha)
    print()
    
    restart=input('Do you want to create another character?: ')
    if restart=='no' or restart=='n' or restart=='No' or restart=='N' or restart=='NO' or restart=='n o' or restart=='N O' or restart=='N o':
        cont=False
