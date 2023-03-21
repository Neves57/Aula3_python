#1)Calculador de média

m1 = float(input('Nota da matéria 1:\n'))
m2 = float(input('Nota da matéria 2:\n'))
m3 = float(input('Nota da matéria 3:\n'))

if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('Aprovado!')
else:
    print('Reprovado.')

#2)Calcula se precisa ou não pagar imposto

s = float(input('Qual é o seu salário?'))
b = 1200
if s > b:
    print("Paga imposto!")
else:
    print('Não paga imposto!')

