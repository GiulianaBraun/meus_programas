valor = int(input('Digite o valor:'))
notas100 = valor // 100
resto = valor % 100
notas50 = resto // 50
resto = resto % 50
notas20 = resto // 20
resto = resto % 20
notas10 = resto // 10
resto = resto % 10
notas5 = resto // 5
resto = resto % 5
print ('Notas de 100: %d' %notas100)
print ('Notas de 50: %d' %notas50)
print ('Notas de 20: %d' %notas20)
print ('Notas de 20: %d' %notas10)
print ('Notas de 5: %d' %notas5)

