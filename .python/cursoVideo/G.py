# partida de futeboll 

print('============')
print('MENGÃO x VASCO')
print('============')

gols1 = int(input('quantos gols o mengão fez? '))
gols2 = int(input('quantos gols o vascão fez? '))

diferenca = abs(gols1 - gols2) # abs pega o módulo do número

print('============')

if diferenca >3:
    print(f'''DIFERENÇA: {diferenca}
        STATUS: GOLEADA ''')
elif diferenca == 3: 
    print(f'''DIFERENÇA: {diferenca}
        STATUS: PARTIDA NORMAL ''')
else: 
    print(f'''DIFERENÇA: {diferenca}
        STATUS: EMPATE ''')
