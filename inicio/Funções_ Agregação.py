# vai contar a quantidade de linhas
resultado = cursor.execute('''select COUNT(*)
from zoologico''').fetchall()
print(resultado)

# vai mostrar a maior elemento
resultado = cursor.execute('''select MAX(idade)
from zoologico''').fetchall()
print(f"A maior idade é {resultado}")

# MEDIA DOS ELEMENTOS
resultado = cursor.execute('''select AVG(idade)
from zoologico''').fetchall()
print(f"A media é : {resultado}")

#MENOR ELEMENTO DA TABELA
resultado = cursor.execute('''select MIN(idade)
from zoologico''').fetchall()
print(f"O MENOR IDADE É : {resultado}")

# A SOMA DOS VALORES
resultado = cursor.execute('''select sum(idade)
from zoologico''').fetchall()
print(f"a soma dos valores é : {resultado}")
