#06: Aproveitamento de um aluno  

# calcular média e mostrar classificação  
 
print('===BOLETIM ESCOLAR===') 

Nota1= float(input('digite sua primeira nota: '))  

Nota2= float(input('digite sua segunda nota: ')) 

Media = (Nota1 + Nota2) * 100 / 2

if 900<= Media <=1000:   
    print(f' MÉDIA: {Media:.1f} ')  
    print('APROVEITAMENTO: A ' ) 
elif 800<= Media <890: 
    print(f'MÉDIA: {Media:.1f}')
    print('APROVEITAMENTO: B ' ) 
elif 700<= Media <790: 
    print(f'MÉDIA: {Media:.1f}')
    print('APROVEITAMENTO: C ' )
elif 600<= Media <690: 
    print(f'MÉDIA: {Media:.1f}')
    print('APROVEITAMENTO: D ' )
elif 500<= Media <=590: 
    print(f'MÉDIA: {Media:.1f}')
    print('APROVEITAMENTO: E ' )
else:
    print(f'MÉDIA: {Media:.1f}')
    print('APROVEITAMENTO: F ')