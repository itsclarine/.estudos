#05: empréstimo | 20% 

# algoritmo para calcular parcelas e acréscimo de 20% sob o valor  

Emp = int(input('digite o valor do empréstimo: ')) 

Parcelas = int(input('quantas parcelas: '))  

A = Emp * 1.20 

Pa = A / Parcelas  

print(f' você pagará {Parcelas} parcelas de R${Pa:.2f}') 